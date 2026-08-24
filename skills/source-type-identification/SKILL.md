---
name: source-type-identification
type: skill
description: Identifies and explains the likely type of a supplied source while preserving uncertainty and verification needs.
tags: [research, sources, verification]
audience: [researchers, educators, students]
status: experimental
version: 0.1.0
maintainer: CIE / unassigned
last_reviewed: 2026-08-24
---

# Source type identification

## Intended outcome

A justified classification of a source that helps a user judge its role and evidential limits. It does not determine quality from format alone.

## Trigger and use conditions

Use when a source, citation, excerpt, landing page or document needs classification. Do not infer peer-review status, study design or authority solely from appearance.

## Workflow

1. Inspect the supplied record and list observable features: authorship, publisher, venue, date, structure, methods, identifiers and references.
2. Distinguish publication type from research design and evidence type.
3. Classify at the narrowest level supported by the evidence, such as journal article, preprint, policy document, evidence synthesis, empirical study or commentary.
4. State the clues supporting the classification and plausible alternatives.
5. Identify properties that require external verification, including peer-review status, retractions, version of record and publisher identity.
6. Explain what the source type can and cannot imply for the user's purpose.

## Inputs and outputs

Input is a source or bibliographic record plus, where relevant, the user's purpose. Output includes likely source type, confidence, observable evidence, unresolved properties, verification steps and use implications.

## Constraints and quality checks

- Never invent bibliographic details.
- Do not treat a DOI, polished PDF or academic language as proof of peer review.
- Separate direct observation, classification and inference.
- Use calibrated confidence and name competing classifications when needed.
- Recommend checking the publisher or authoritative index for consequential use.

## Failure and uncertainty behaviour

If only a title or fragment is supplied, provide a provisional classification and request the minimum additional evidence. If conflicting versions exist, avoid selecting one as authoritative without verification.

## Example

A manuscript with an abstract, methods and DOI may be an empirical preprint rather than a peer-reviewed journal article. Report both the likely research design and the unresolved publication status.
