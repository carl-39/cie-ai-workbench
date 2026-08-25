---
name: Verify source metadata
type: skill
description: Extracts bibliographic metadata and verifies material fields against appropriate authoritative records while preserving discrepancies and uncertainty.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-25
tags:
  - metadata-verification
  - source-identification
  - bibliography
audience:
  - Researchers
  - Students
  - Research support staff
---

# Verify Source Metadata

> This skill is experimental. A clean metadata record remains bounded by the sources checked and does not establish source quality or suitability by itself.

Extract provisional metadata, identify the source and version, verify each material field against authoritative records, and return both a clean record and an evidence-rich audit table. Adapt explanations to the user while preserving research-grade precision.

## Core rules

- Always extract and verify. Never present extracted metadata alone as verified.
- Preserve extracted and verified values separately. Never silently overwrite a discrepancy.
- Adapt the field schema to the source type and capture every bibliographically meaningful field available.
- Keep different versions, editions, manifestations, releases, preprints, accepted manuscripts, and versions of record separate. Describe a possible relationship without merging records unless identity is strongly established.
- Report missing, ambiguous, conflicting, or unverifiable fields. Recommend specific next steps; do not invent or infer missing values.
- Remain focused on metadata. Do not generate a formatted reference or in-text citation unless the user separately requests that work outside this skill.
- Use concise language by default. Explain terminology and implications when the user appears unfamiliar or asks for guidance.

## Workflow

### 1. Inspect the input

Accept documents, images, screenshots, title or copyright pages, source records, pasted citations or metadata, identifiers, URLs, and partial details.

- Extract visible and embedded text where available.
- Record the supplied entry point and any limits, such as a cropped page or inaccessible URL.
- Identify candidate source type, subtype, and version before selecting a schema.
- If the source is unsupported or unusual, use an extensible `other` type and describe its defining features.

### 2. Build a provisional record

Read [references/metadata-fields-and-authorities.md](references/metadata-fields-and-authorities.md) and select all fields relevant to the candidate source type. Preserve wording, ordering, diacritics, punctuation, dates, identifiers, and contributor roles as displayed in the supplied source.

Assign every extracted field an initial status of `unverified`. Mark absent expected fields as `missing`; do not fill them by inference.

### 3. Establish source identity

Use the strongest available identifiers first. Normalise identifiers only for matching while retaining the displayed form.

- Test DOI, ISBN, ISSN, handle, repository identifier, database accession, canonical URL, video ID, or other persistent identifier.
- Otherwise match on a combination of title, creator, date, container, publisher or institution, and version indicators.
- Treat close title similarity as insufficient when creators, dates, editions, versions, or containers differ.
- If identity remains uncertain, verify only what can be supported and label the record `ambiguous`.

### 4. Verify through the authority hierarchy

Use active lookup when tools permit. Follow the source-specific hierarchy in the reference file, applying these general priorities:

1. Identifier registration or issuing record, such as Crossref, DataCite, an ISBN agency record, or the platform's canonical item record
2. Authoritative publisher, journal, issuing organisation, conference, repository, institutional, or creator-platform page
3. National, university, or trusted union library catalogue
4. Reputable disciplinary index or bibliographic database
5. Other credible secondary records, used as supporting evidence rather than as definitive authority

Prefer primary and authoritative records, but do not assume the highest-ranked source is complete or error-free. Run a second-source check when:

- records conflict;
- source identity or version is uncertain;
- a key field has low confidence;
- the primary record is incomplete, malformed, or internally inconsistent.

Do not treat search-result snippets, user-edited aggregators, citation generators, retail listings, or copied reference lists as authoritative verification.

### 5. Compare field by field

Use one of these statuses for each field:

- `matched`: extracted and verified values agree, allowing harmless normalisation
- `corrected`: an authoritative value materially differs from the extracted value
- `unverified`: no adequate authoritative evidence was found
- `missing`: the field is expected or useful but absent from the supplied source and authoritative records
- `ambiguous`: evidence supports more than one interpretation or record

Rate confidence as `high`, `medium`, or `low`, based on identity strength, authority, agreement across records, and completeness. A high-confidence record may still contain individual low-confidence fields.

### 6. Return both output formats

Start with a brief identification statement containing source type, likely version or manifestation, overall verification outcome, and any consequential warning.

#### Clean verified metadata record

Present a structured, reusable record adapted to the source type. Use the verified value for matched or corrected fields. Clearly label unverified or ambiguous values; do not make the clean record appear more certain than the evidence.

#### Field-level verification table

Use these columns:

| Field | Extracted value | Verified value | Status | Evidence | Confidence |
|---|---|---|---|---|---|

Link evidence directly when possible and name the authority. Preserve both values when they differ.

After the table, add only the applicable sections:

- **Version relationships:** Distinguish related records without merging them.
- **Unresolved issues:** Explain conflicts, gaps, or access limitations.
- **Recommended next steps:** Specify the most useful action or missing input, such as supplying a copyright page, checking a DOI, locating a repository record, or confirming an edition.

## Quality checks

Before responding, confirm that:

- extraction and verification were both attempted;
- the schema fits the source type;
- identifiers resolve to the same work and version being described;
- extracted values remain visible wherever authoritative values differ;
- every claim of correction cites adequate evidence;
- no distinct versions or editions were merged;
- gaps are labelled rather than inferred;
- both the clean record and audit table are present.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-25 | Imported as an experimental skill package and aligned with CIE AI Workbench metadata. |
