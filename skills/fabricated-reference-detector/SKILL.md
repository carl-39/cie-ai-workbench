---
name: Fabricated reference detector
type: skill
description: Audits references and in-text citations for verified identity, material discrepancies and fabrication risk without treating database absence as proof.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-25
tags:
  - reference-verification
  - citation-audit
  - research-integrity
audience:
  - Researchers
  - Academic staff
  - Students
  - Research support staff
---

# Fabricated Reference Detector

> This skill is experimental. Its classifications support evidence review; they are not automatic findings of misconduct and must not be converted into allegations about a person.

Audit citations without overclaiming. Preserve each submitted reference exactly as written, verify its identity and material details, classify it cautiously, and present corrections separately.

## Core safeguards

- Never equate `not found` with `fabricated`.
- Never invent a replacement DOI, source, creator, title, date, or publication detail.
- Preserve submitted text verbatim. Do not silently repair it.
- Separate verified facts from suggested corrections and APA 7 formatting.
- Verify the work and cited version, not merely a similar title.
- Use direct evidence links for consequential findings.
- State access, indexing, language, age, regional, and search limitations.
- Treat citation accuracy as distinct from source quality, peer-review status, and academic suitability.
- Never use a classification as the sole basis for a misconduct decision or allegation; consequential conclusions require appropriate human review and institutional process.

## Choose the audit depth

Adapt automatically.

### Rapid screening

Use for routine checks, large initial scans, or a requested quick review.

1. Parse and deduplicate entries without altering the originals.
2. Test supplied persistent identifiers.
3. Search the strongest relevant authority plus one corroborating source where practical.
4. Flag identity failures, material metadata conflicts, and citation-list mismatches.
5. Escalate suspicious, ambiguous, or conflicting entries to forensic verification.

### Forensic verification

Use for suspected fabrication, formal audits, consequential decisions, conflicting records, low-confidence identity, explicit requests, or escalated entries.

1. Establish source type and candidate identity.
2. Search multiple relevant authorities using identifiers, titles, creators, dates, containers, publishers or institutions, and distinctive metadata combinations.
3. Investigate alternate spellings, transliteration, editions, versions, corrections, retractions, title changes, online-first dates, and repository copies when relevant.
4. Compare material fields individually and document positive and negative search evidence.
5. Seek a second independent source whenever records conflict or confidence is low.

Read [references/verification-framework.md](references/verification-framework.md) before either audit. Apply its authority hierarchy, classification thresholds, material-field rules, and evidence standards.

## Workflow

### 1. Inspect and preserve the input

Accept a pasted reference, reference list, DOI, URL, ISBN or other identifier, suspected citation, or uploaded document. Extract references and in-text citations when requested or when a document audit implies both.

- Assign stable item IDs such as `R01` and citation-cluster IDs such as `C01`.
- Preserve every reference exactly as submitted, including apparent errors.
- Record extraction uncertainty for scans, columns, footnotes, tables, OCR, or broken line wraps.
- Keep distinct references separate even when they appear to describe the same work.

### 2. Reconcile citations and references

When in-text citations are present:

- map author-date and narrative citations to candidate entries;
- flag citations with no reference-list entry;
- flag entries never cited in the inspected text;
- flag year, creator, suffix, group-author, spelling, and multi-work inconsistencies;
- distinguish matching problems from evidence that a source is fabricated.

Do not claim an entry is uncited unless the entire relevant text was inspected.

### 3. Establish the claimed source

Identify source type, work, container, version, and supplied identifiers. Normalise identifiers only for lookup while retaining their submitted form. Resolve identifiers first, but confirm that the record matches the claimed work. A DOI attached to a different work is a major discrepancy, not verification.

### 4. Search and triangulate

Follow the authority hierarchy in the reference file. Prefer registries, official publishers or issuing bodies, canonical platform records, repositories, library catalogues, and disciplinary indexes over aggregators or snippets.

- Use a second source for conflicts, suspected fabrication, or low confidence.
- Search beyond exact strings because a real reference may contain transcription errors.
- Record sources and query variants checked for `Unverified`, `Likely fabricated`, and `Definitely fabricated` outcomes.
- Treat inaccessible pages, incomplete coverage, and database silence as limitations.

### 5. Compare material details

Check identity and retrieval fields as applicable: creators; title; date; journal, book, proceedings, series, platform, publisher, institution, or issuing body; volume, issue, edition, pages, article or report number, or degree; DOI, ISBN, ISSN, URL, handle, accession, repository, dataset, or media ID; and version or publication status.

Distinguish harmless style differences from material discrepancies. Apply APA 7 only after identity and metadata verification.

### 6. Classify cautiously

Assign exactly one classification per reference:

- **Verified**
- **Verified with discrepancies**
- **Unverified**
- **Likely fabricated**
- **Definitely fabricated**

Also assign `High`, `Moderate`, or `Low` confidence and a concise rationale. Use `Definitely fabricated` only with conclusive evidence; it should be rare. If evidence cannot distinguish a damaged real citation from an invented one, use `Unverified` or `Likely fabricated` as warranted.

### 7. Construct corrections separately

For an identifiable work, provide:

1. verified metadata supported by cited evidence;
2. suggested corrections, with changed fields explicit; and
3. a corrected APA 7 reference only when enough metadata is verified.

Label incomplete references as drafts and use bracketed field labels rather than invented values. If multiple candidate works fit, show them and do not choose without evidence.

## Output

Adapt detail to audit size. For larger audits, use these sections.

### Overall risk summary

Report counts by classification, consequential patterns, audit depth, scope, and limitations. Do not convert classifications into allegations about the author or student.

### Reference verification

| ID | Submitted reference | Classification | Key finding | Confidence | Evidence |
|---|---|---|---|---|---|

Keep the submitted reference verbatim and link authoritative evidence.

### In-text citation reconciliation

Include only when citations were inspected.

| Citation ID | In-text citation | Matched reference | Status | Issue or action |
|---|---|---|---|---|

### Evidence notes

Expand problematic or uncertain entries by default. Include sources searched, decisive matches or conflicts, negative-search limits, and the classification rationale.

### Verified facts and suggested corrections

For each applicable item, separate:

- **Verified facts:** Evidence-supported metadata.
- **Suggested corrections:** Proposed changes and their basis.
- **Corrected APA 7 reference:** Only when sufficiently supported.
- **Next step:** The most useful action if uncertainty remains.

### Structured export

Offer or provide CSV for tabular workflows and JSON when requested or useful for a large audit. Use the reference-file schema. Never omit evidence, confidence, limitations, or submitted text.

## Quality check

Confirm that every submitted reference remains visible and unchanged; classifications meet their thresholds; serious findings have traceable evidence; two sources were checked where required; negative searches are not presented as proof; citation mismatches are not conflated with fabrication; corrections are separate from verified facts; APA 7 references contain no invented metadata; and limitations and next steps are explicit.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-25 | Imported as an experimental skill package, aligned with CIE AI Workbench metadata and bounded against automated misconduct findings. |
