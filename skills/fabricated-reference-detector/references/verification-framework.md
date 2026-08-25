# Verification Framework

## Contents

1. Classification thresholds
2. Evidence and confidence
3. Authority hierarchy by source type
4. Material discrepancies
5. Negative-finding search protocol
6. Citation reconciliation
7. Structured export schema

## 1. Classification thresholds

### Verified

Use when authoritative evidence establishes the claimed work and its core identity fields agree. Harmless punctuation, capitalisation, abbreviated container titles, URL forms, or APA-style differences do not prevent this classification.

### Verified with discrepancies

Use when the work exists, but submitted details are materially wrong or incomplete. Examples include a wrong year, creator order, journal, volume, pages, edition, title, or DOI. State whether the discrepancy affects retrieval or attribution.

### Unverified

Use when evidence is insufficient to confirm or refute the claimed work. Reasons may include incomplete metadata, inaccessible or non-indexed sources, limited coverage, language or regional gaps, unpublished material, or several plausible candidates. This is not evidence of fabrication.

### Likely fabricated

Use only when multiple independent warning signals make fabrication more plausible than ordinary citation error. Normally require all of:

- no credible record after a documented multi-route, multi-source search;
- material details that do not form a coherent publication identity; and
- positive contradictions, such as a DOI resolving elsewhere, an impossible volume-year combination, a nonexistent claimed issue, or authoritative creator-title-container conflicts.

Explain plausible alternatives such as corruption, conflation, or hallucinated metadata.

### Definitely fabricated

Reserve for conclusive evidence, such as a formal confirmation from the claimed publisher or journal, direct provenance evidence of invention, or a demonstrably impossible combination of elements from different identifiable works. Database silence alone never meets this threshold.

## 2. Evidence and confidence

- **High:** Strong identifiers or primary records agree; decisive conflicts are conclusive; search coverage is appropriate.
- **Moderate:** Well supported, but one relevant authority, version detail, or record remains unavailable.
- **Low:** Evidence is indirect, coverage is weak, identity is ambiguous, or important conflicts remain.

Prefer record-level evidence over snippets. Cite the exact item or registry page when possible. Distinguish a matching record or direct contradiction from a negative search. Negative search evidence has limited weight because coverage is incomplete.

## 3. Authority hierarchy by source type

### Journal articles, preprints, and conference works

1. DOI or disciplinary identifier registry
2. Publisher, journal, proceedings, or conference record
3. Canonical preprint or institutional repository
4. Relevant disciplinary index
5. OpenAlex, DOAJ, or trusted library discovery

Confirm title, creators, container, year, volume or issue, locator, DOI, and version. A DOI does not itself establish peer review or quality.

### Books and chapters

1. Publisher or official book record
2. ISBN agency or national library
3. Trusted union or university library catalogue
4. DOI registry for DOI-bearing books or chapters
5. Scholarly indexes

Match edition, format, chapter-versus-book identity, editors, pages, publisher, and ISBN manifestation. Do not reject older or regional works for lacking a DOI.

### Theses and dissertations

1. Awarding institution repository or catalogue
2. National thesis service or authoritative dissertation database
3. Library catalogue or persistent handle record
4. Scholarly indexes

### Reports, standards, policies, and grey literature

1. Issuing organisation or standards body
2. Government, intergovernmental, institutional, or archival repository
3. Persistent identifier registry
4. National or university library catalogue
5. Trusted secondary index

Account for withdrawn, superseded, archived, and revised versions.

### Datasets and software

1. Data or software identifier registry
2. Canonical repository or release page
3. Responsible institution or creator record
4. Scholarly index or citing publication

Match version, release date, creators, repository, and identifier.

### Webpages and online publications

1. Canonical page and responsible organisation
2. Official archive or preserved snapshot
3. Issuing organisation's publication index or repository
4. Trusted catalogue or secondary record

Account for title changes, redirects, deleted pages, and dynamic dates. A dead URL is not proof that a page never existed.

### Videos, podcasts, and audiovisual works

1. Canonical platform item or publisher or broadcaster record
2. Creator or production organisation's official record
3. Episode feed, catalogue, archive, or persistent media identifier
4. Trusted secondary catalogue

Match title, contributor roles, series, date, publisher or platform, and media ID. Distinguish a work from its host.

## 4. Material discrepancies

Material discrepancies affect identity, attribution, chronology, version, or retrieval. Examples include an identifier resolving elsewhere; a creator absent from the authoritative record; a title pointing to another work; a wrong container or institution; incompatible volume, issue, locator, edition, or year; a preprint represented as the version of record; or an ISBN belonging to another edition.

Treat typography, capitalisation, punctuation, DOI URL presentation, and style-driven omissions as non-material unless they impede identification.

## 5. Negative-finding search protocol

Before assigning `Likely fabricated`:

1. Resolve and search each identifier.
2. Search the exact title.
3. Search distinctive title fragments with the first creator surname.
4. Search creator, year, and container or publisher.
5. Search the claimed journal, publisher, or institution directly.
6. Search plausible spelling, transliteration, date, and title variants.
7. Check editions, versions, repositories, archives, and online-first records.
8. Check at least two independent authoritative sources.

Document sources and important query variants. Stop when identity is established; do not manufacture certainty through repetitive searching.

## 6. Citation reconciliation

Use `matched`, `in-text citation missing from reference list`, `reference-list entry not found in inspected text`, `creator mismatch`, `year mismatch`, `year-suffix mismatch`, `ambiguous match`, or `extraction uncertain`.

For grouped citations, split works while preserving the original cluster. Allow legitimate `et al.` shortening and group-author abbreviations. Determine same-author same-year suffixes only after establishing the reference set.

## 7. Structured export schema

```json
{
  "id": "R01",
  "submitted_reference": "",
  "source_type": "",
  "audit_depth": "rapid|forensic",
  "classification": "Verified|Verified with discrepancies|Unverified|Likely fabricated|Definitely fabricated",
  "confidence": "High|Moderate|Low",
  "verified_identity": {},
  "material_discrepancies": [],
  "evidence": [
    {"authority": "", "url": "", "finding": "", "evidence_type": "positive|negative-search"}
  ],
  "search_limitations": [],
  "suggested_corrections": [],
  "corrected_apa7_reference": null,
  "next_steps": [],
  "citation_links": []
}
```

For CSV, flatten arrays with semicolons and retain the same conceptual fields. Use a separate citation-reconciliation table when practical.
