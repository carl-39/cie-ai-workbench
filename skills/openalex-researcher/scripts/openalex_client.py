#!/usr/bin/env python3
"""Small OpenAlex API client for literature search, bibliometric grouping, and exports.

Authentication: set OPENALEX_API_KEY in the environment. The script never stores or
prints the key.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Iterable, List, Optional

BASE_URL = "https://api.openalex.org"
MAX_ATTEMPTS = 3
BACKOFF_SECONDS = 0.5
MAX_BACKOFF_SECONDS = 4.0


def reconstruct_abstract(inv: Optional[Dict[str, List[int]]]) -> str:
    if not inv:
        return ""
    positions: Dict[int, str] = {}
    for word, indexes in inv.items():
        for idx in indexes:
            positions[idx] = word
    return " ".join(positions[i] for i in sorted(positions))


def compact_authors(work: Dict[str, Any], limit: int = 3) -> str:
    names = []
    for authorship in work.get("authorships", []) or []:
        author = authorship.get("author") or {}
        name = author.get("display_name")
        if name:
            names.append(name)
    if not names:
        return ""
    if len(names) > limit:
        return ", ".join(names[:limit]) + ", et al."
    return ", ".join(names)


def source_name(work: Dict[str, Any]) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    return source.get("display_name") or ""


def best_oa_url(work: Dict[str, Any]) -> str:
    oa = work.get("open_access") or {}
    if oa.get("oa_url"):
        return oa.get("oa_url")
    primary = work.get("primary_location") or {}
    if primary.get("landing_page_url"):
        return primary.get("landing_page_url")
    return work.get("doi") or work.get("id") or ""


def normalize_work(work: Dict[str, Any]) -> Dict[str, Any]:
    oa = work.get("open_access") or {}
    return {
        "openalex_id": work.get("id", ""),
        "title": work.get("title") or work.get("display_name") or "",
        "year": work.get("publication_year") or "",
        "type": work.get("type") or "",
        "authors": compact_authors(work),
        "source": source_name(work),
        "cited_by_count": work.get("cited_by_count", 0),
        "doi": work.get("doi") or "",
        "is_oa": oa.get("is_oa", False),
        "oa_status": oa.get("oa_status") or "",
        "oa_url": best_oa_url(work),
        "abstract": reconstruct_abstract(work.get("abstract_inverted_index")),
    }


def markdown_cell(value: Any) -> str:
    """Escape untrusted API text for a Markdown table cell."""
    text = str(value).replace("\r", " ").replace("\n", " ")
    return html.escape(text, quote=False).replace("|", "\\|")


def request_json(path: str, params: Dict[str, Any], sleep: float = 0.1) -> Dict[str, Any]:
    api_key = os.environ.get("OPENALEX_API_KEY")
    if not api_key:
        raise SystemExit("OPENALEX_API_KEY is required for OpenAlex requests.")
    clean_params = {k: v for k, v in params.items() if v not in (None, "", [])}
    clean_params["api_key"] = api_key
    query = urllib.parse.urlencode(clean_params, doseq=True)
    url = f"{BASE_URL}/{path.lstrip('/')}"
    if query:
        url = f"{url}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "openalex-researcher-skill/1.0"})
    for attempt in range(MAX_ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                data = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if retryable and attempt < MAX_ATTEMPTS - 1:
                retry_after = exc.headers.get("Retry-After") if exc.headers else None
                delay = float(retry_after) if retry_after and retry_after.isdigit() else BACKOFF_SECONDS * (2**attempt)
                delay = min(delay, MAX_BACKOFF_SECONDS)
                time.sleep(delay)
                continue
            detail = exc.read().decode("utf-8", errors="replace").replace(api_key, "[REDACTED]")
            raise SystemExit(f"OpenAlex HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(BACKOFF_SECONDS * (2**attempt))
                continue
            reason = str(exc.reason).replace(api_key, "[REDACTED]")
            raise SystemExit(f"OpenAlex request failed: {reason}") from exc
    if sleep:
        time.sleep(sleep)
    return data


def build_filter(args: argparse.Namespace) -> str:
    filters: List[str] = []
    if getattr(args, "filter", None):
        filters.extend(args.filter)
    if getattr(args, "from_year", None) and getattr(args, "to_year", None):
        filters.append(f"publication_year:{args.from_year}-{args.to_year}")
    elif getattr(args, "from_year", None):
        filters.append(f"publication_year:>{int(args.from_year) - 1}")
    elif getattr(args, "to_year", None):
        filters.append(f"publication_year:<{int(args.to_year) + 1}")
    if getattr(args, "type", None):
        filters.append(f"type:{args.type}")
    if getattr(args, "open_access", False):
        filters.append("is_oa:true")
    return ",".join(filters)


def print_markdown_works(rows: List[Dict[str, Any]]) -> None:
    print("| # | Work | Year | Authors | Source | Cited by | DOI | OA |")
    print("|---|------|------|---------|--------|----------|-----|----|")
    for idx, row in enumerate(rows, 1):
        title = markdown_cell(row["title"] or "Untitled")
        doi = row["doi"] or row["openalex_id"]
        oa = "yes" if row["is_oa"] else "no"
        cells = [row["year"], row["authors"], row["source"], row["cited_by_count"], doi, oa]
        year, authors, source, cited_by, identifier, oa_value = map(markdown_cell, cells)
        print(f"| {idx} | {title} | {year} | {authors} | {source} | {cited_by} | {identifier} | {oa_value} |")


def write_csv(path: str, rows: Iterable[Dict[str, Any]]) -> None:
    rows = list(rows)
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def search_works(args: argparse.Namespace) -> None:
    params = {
        "search": args.query,
        "filter": build_filter(args),
        "sort": args.sort,
        "per_page": max(1, min(args.per_page, 100)),
        "select": args.select,
    }
    data = request_json("works", params)
    rows = [normalize_work(work) for work in data.get("results", [])]
    if args.export_csv:
        write_csv(args.export_csv, rows)
    if args.export_json:
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print_markdown_works(rows)


def group_works(args: argparse.Namespace) -> None:
    params = {
        "search": args.query,
        "filter": build_filter(args),
        "group_by": args.group_by,
        "per_page": max(1, min(args.per_page, 100)),
    }
    data = request_json("works", params)
    groups = data.get("group_by", [])
    if args.export_json:
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(groups, f, ensure_ascii=False, indent=2)
    if args.format == "json":
        print(json.dumps(groups, ensure_ascii=False, indent=2))
    else:
        print("| Key | Display name | Count |")
        print("|---|---|---:|")
        for group in groups:
            key = markdown_cell(group.get("key", ""))
            name = group.get("key_display_name") or group.get("key") or ""
            count = markdown_cell(group.get("count", 0))
            print(f"| {key} | {markdown_cell(name)} | {count} |")


def get_entity(args: argparse.Namespace) -> None:
    entity = args.entity.strip("/")
    data = request_json(f"{entity}/{args.id}", {})
    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        heading = markdown_cell(data.get("display_name") or data.get("title") or data.get("id"))
        print(f"# {heading}\n")
        print(json.dumps(data, ensure_ascii=False, indent=2)[:4000])


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Query OpenAlex for scholarly literature and bibliometrics.")
    sub = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--query", help="OpenAlex full-text search query")
    common.add_argument("--filter", action="append", help="Raw OpenAlex filter expression; repeatable")
    common.add_argument("--from-year", type=int, help="Earliest publication year")
    common.add_argument("--to-year", type=int, help="Latest publication year")
    common.add_argument("--type", help="Work type, e.g. article, book, dataset")
    common.add_argument("--open-access", action="store_true", help="Filter to open access works")
    common.add_argument("--per-page", type=int, default=25, help="Results per page, max 100")
    common.add_argument("--format", choices=["markdown", "json"], default="markdown")
    common.add_argument("--export-json", help="Write normalized JSON to this path")

    p_search = sub.add_parser("search-works", parents=[common], help="Search OpenAlex works")
    p_search.add_argument("--sort", default=None, help="OpenAlex sort, e.g. cited_by_count:desc")
    p_search.add_argument("--select", default=None, help="Comma-separated fields to select")
    p_search.add_argument("--export-csv", help="Write normalized CSV to this path")
    p_search.set_defaults(func=search_works)

    p_group = sub.add_parser("group-works", parents=[common], help="Group OpenAlex works for bibliometrics")
    p_group.add_argument("--group-by", required=True, help="OpenAlex group_by field, e.g. publication_year")
    p_group.set_defaults(func=group_works)

    p_get = sub.add_parser("get", help="Retrieve a single OpenAlex entity")
    p_get.add_argument(
        "--entity",
        required=True,
        choices=["works", "authors", "sources", "institutions", "topics", "keywords", "publishers", "funders"],
    )
    p_get.add_argument("--id", required=True, help="OpenAlex ID or supported external ID shorthand")
    p_get.add_argument("--format", choices=["markdown", "json"], default="json")
    p_get.set_defaults(func=get_entity)

    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
