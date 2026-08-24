#!/usr/bin/env python3
"""Validate lightweight YAML front matter on Workbench assets."""

from __future__ import annotations

import datetime as dt
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
TYPE_FILES = {
    "prompts": "README.md",
    "skills": "SKILL.md",
    "agents": "README.md",
    "patterns": "README.md",
}
STATUSES = {"experimental", "testing", "approved", "deprecated"}
REQUIRED = {"name", "type", "description", "status", "version", "maintainer", "last_reviewed"}
VERSION = re.compile(r"^\d+\.\d+\.\d+$")


def validate(path: pathlib.Path, expected_type: str) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{path.relative_to(ROOT)}: missing YAML front matter"]
    try:
        raw = text.split("---\n", 2)[1]
        data = yaml.safe_load(raw) or {}
    except (ValueError, yaml.YAMLError) as exc:
        return [f"{path.relative_to(ROOT)}: invalid YAML: {exc}"]
    metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
    asset_data = {**data, **metadata}
    missing = REQUIRED - asset_data.keys()
    if missing:
        errors.append(f"missing fields: {', '.join(sorted(missing))}")
    if asset_data.get("type") != expected_type:
        errors.append(f"type must be {expected_type!r}")
    if asset_data.get("status") not in STATUSES:
        errors.append("status is not recognised")
    if not VERSION.fullmatch(str(asset_data.get("version", ""))):
        errors.append("version must use MAJOR.MINOR.PATCH")
    reviewed = asset_data.get("last_reviewed")
    if isinstance(reviewed, dt.date):
        reviewed = reviewed.isoformat()
    try:
        dt.date.fromisoformat(str(reviewed))
    except ValueError:
        errors.append("last_reviewed must be YYYY-MM-DD")
    return [f"{path.relative_to(ROOT)}: {error}" for error in errors]


def main() -> int:
    errors: list[str] = []
    for directory, filename in TYPE_FILES.items():
        expected_type = directory[:-1] if directory != "skills" else "skill"
        for asset_dir in sorted((ROOT / directory).iterdir()):
            if not asset_dir.is_dir() or asset_dir.name.startswith("_"):
                continue
            primary = asset_dir / filename
            if not primary.exists():
                errors.append(f"{asset_dir.relative_to(ROOT)}: missing {filename}")
                continue
            errors.extend(validate(primary, expected_type))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Asset metadata is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
