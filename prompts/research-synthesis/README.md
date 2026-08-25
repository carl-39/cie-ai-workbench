---
name: Research synthesis
type: prompt
description: Synthesises supplied research material into a structured, traceable response without inventing evidence.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-24
tags:
  - research
  - synthesis
  - evidence
audience:
  - Researchers
  - Academic staff
---

# Research synthesis

> **Starter example:** this experimental prompt demonstrates the repository structure. It is not an approved CIE production asset.

## Purpose

Help a researcher turn supplied notes or sources into a coherent synthesis while preserving the distinction between source-supported claims, interpretation and unresolved gaps.

## Intended users

Researchers and academic staff who can assess the underlying sources and verify the resulting synthesis.

## Use cases

- Compare themes, findings or positions across a defined source set.
- Produce a structured briefing from research notes.
- Identify agreement, disagreement and evidence gaps before drafting.

## Ready-to-use prompt

```text
You are supporting a research synthesis using only the material I supply.

Research question or purpose:
{{research_question}}

Source material:
{{source_material}}

Audience and intended use:
{{audience_and_use}}

Requested format or length (optional):
{{format_or_length}}

Instructions:
1. Synthesize the material around the research question; do not produce a
   source-by-source list unless comparison requires it.
2. Use only claims supported by the supplied material. Do not invent sources,
   quotations, findings, page numbers or bibliographic details.
3. Distinguish clearly between evidence reported by the sources, your synthesis
   or inference, and questions the supplied material cannot answer.
4. Identify important convergence, divergence, qualifications and gaps.
5. Preserve source labels exactly as supplied so every substantive claim can be
   traced back for human verification.
6. If source labels or essential context are missing, state what is missing and
   ask for it before making a claim that depends on it.
7. End with a verification table containing: synthesis claim, supporting source
   label(s), and what the user should check in the original source.

Return:
- a concise synthesis;
- key convergences and divergences;
- limitations and unanswered questions; and
- the verification table.
```

## Inputs

### Required

- `research_question`: the focus or purpose of the synthesis.
- `source_material`: labelled excerpts, notes or source texts available for use.
- `audience_and_use`: who will read the output and what they will do with it.

### Optional

- `format_or_length`: desired structure, emphasis or approximate length.

## Expected output

A thematic synthesis with traceable source labels, visible uncertainty, stated limitations and a verification table. It should not imply that source quality has been assessed unless that evaluation was supplied.

## Model or tool assumptions

The prompt is provider-flexible but requires a model context large enough for the supplied material. Retrieval or browsing is not assumed.

## Limitations

- Output quality depends on the completeness, accuracy and labelling of supplied material.
- The prompt does not perform a systematic literature review or independent source-quality appraisal.
- Long source sets may exceed tool context limits or lead to uneven coverage.

## Verification requirements

The user must check substantive claims, quotations and interpretations against the original sources before publication, teaching use or consequential decision-making. Verify that omitted sources do not materially change the synthesis.

## Responsible AI considerations

Remove personal or confidential information unless its use is authorised. Respect access and copyright restrictions on source material. Disclose AI assistance where required, and do not use the output to bypass assessment rules or substitute for scholarly judgement.

## Example

For an input set labelled `S1`, `S2` and `S3`, a claim in the synthesis should link to those labels rather than an invented author-date citation. The final table should tell the user exactly which original passage or interpretation needs checking.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-24 | Initial experimental starter version. |
