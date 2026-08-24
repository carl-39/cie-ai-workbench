---
name: identify-source-type
description: Inspect URLs, DOIs, uploaded files, pasted citations, and bibliographic metadata to identify the underlying source type for APA 7 referencing. Use when classifying journal articles, books, chapters, webpages, reports, theses, datasets, audiovisual works, preprints, conference works, or ambiguous sources; when distinguishing a work from its hosting platform or repository copy; or when selecting an APA 7 reference template and identifying missing metadata.
metadata:
  type: skill
  tags: [research, sources, apa-7, referencing]
  audience: [researchers, educators, students]
  status: approved
  version: 0.1.0
  maintainer: CIE / unassigned
  last_reviewed: 2026-08-24
---

# Identify Source Type

Identify the work itself, its publication form, and its version. Explain the classification in student-friendly language and also provide a compact structured result for downstream use.

## Workflow

1. Inspect every supplied input: URL, DOI, file, citation, screenshot, or metadata.
2. If a URL or DOI is present, open it and retrieve metadata when tools permit. Follow repository, aggregator, or secondary links to the publisher, institutional repository, DOI record, library catalogue, or other authoritative record where useful.
3. Separate three concepts:
   - **Work:** the intellectual object being referenced.
   - **Publication form:** journal article, report, webpage, thesis, dataset, video, etc.
   - **Host or access point:** ResearchGate, a database, repository, publisher site, YouTube, or another platform.
4. Classify the publication form that determines the APA 7 reference pattern. Do not classify a PDF merely as a PDF or an article merely as a webpage because it appears online.
5. Compare the accessible copy with the authoritative record. Identify preprint, accepted manuscript, version of record, revised edition, or repository copy when evidence permits.
6. Apply the evidence hierarchy below. Resolve contradictions explicitly; do not silently choose one field.
7. Select the closest APA 7 template from `references/source-types.md` and list missing required metadata.
8. Return an ambiguity warning instead of forcing a classification when evidence is inadequate.

## Evidence hierarchy

Prefer evidence in roughly this order, while accounting for context:

1. The content and front matter of the work itself
2. Publisher or issuing-body record
3. DOI registration metadata and authoritative bibliographic records
4. Institutional repository or library catalogue metadata
5. Trusted scholarly indexes and databases
6. The filename, URL path, search snippet, or user-supplied label

Treat file extensions and visual appearance as weak signals. A document with an ISBN is not automatically a book, and a DOI is not proof of a journal article.

## Classification rules

- Identify the most specific defensible type that changes the APA 7 reference structure.
- Distinguish a whole authored book from an edited book and a chapter in an edited book.
- Distinguish journal articles from magazine or newspaper articles, preprints, conference papers, and repository manuscripts.
- Distinguish reports from ordinary webpages using issuing body, document identity, report number, title page, series, and publication context.
- Distinguish theses and dissertations by degree, institution, database or repository, and publication status.
- Treat datasets, software, tests, standards, legislation, audiovisual works, podcasts, social media posts, and generative-AI outputs as distinct types when applicable.
- Classify a dynamically updated reference work or webpage according to its actual function, not its URL alone.
- When a source combines forms, state both levels and identify which level the user is citing. Example: `podcast episode` within a `podcast series`.
- Do not infer unavailable metadata or fabricate bibliographic fields.

## Confidence

Use these labels:

- **High:** multiple authoritative signals agree and no material conflict remains.
- **Moderate:** the classification is well supported but an authoritative record, version detail, or decisive field is unavailable.
- **Low:** classification relies on indirect signals or material conflicts remain.
- **Insufficient evidence:** no defensible classification can be made.

Confidence applies to the classification, not to the general credibility or scholarly quality of the source.

## Output

Use this concise structure:

### Identification

- **Source type:** [specific type]
- **APA 7 category:** [reference category]
- **Confidence:** [High / Moderate / Low / Insufficient evidence]
- **Version/status:** [version of record, preprint, repository copy, unknown, etc.]
- **Host/platform:** [name, if relevant]

### Why

Give two to four decisive clues and identify their provenance. Briefly explain the distinction in student-friendly language.

### APA 7 template

Provide a field-based template, not invented values. Then list:

- **Metadata found:** [fields]
- **Metadata still needed:** [fields]

### Warning

Include only when evidence conflicts, the source is mislabelled, the version differs from the version of record, or the result remains ambiguous. State what would resolve the uncertainty.

### Structured result

Return this compact block when another assistant or workflow may consume the result:

```yaml
source_type: ""
apa7_category: ""
confidence: ""
version_status: ""
host_platform: ""
authoritative_record: ""
evidence:
  - ""
missing_metadata:
  - ""
warnings:
  - ""
```

Omit the structured block when the user clearly wants only a brief human-readable answer.

## Boundaries

- Do not equate source type with source quality, peer-review status, or credibility. Report those only when requested or necessary to correct a misleading label.
- Do not construct a completed reference unless the user asks. Recommend the template and missing fields by default.
- Do not claim that a work is peer reviewed solely because it appears in a journal-like repository or has a DOI.
- If access is blocked, classify from available evidence, lower confidence appropriately, and name the blocked evidence.

Read `references/source-types.md` whenever selecting a category or template, especially for uncommon or borderline sources.
