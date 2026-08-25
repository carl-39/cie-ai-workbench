---
name: Verified research synthesis
type: pattern
description: Combines human source selection and verification with AI-assisted thematic synthesis.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-24
tags:
  - research
  - synthesis
  - human-oversight
audience:
  - Researchers
  - Academic staff
---

# Verified research synthesis

> **Starter example:** this experimental pattern demonstrates a reusable human–AI workflow. It is not an approved CIE production asset.

## Problem

AI can organise a source set quickly, but it may flatten disagreement, overstate evidence or create unsupported references. A useful synthesis therefore needs an explicit chain from human source selection through AI-assisted analysis to human verification.

## Context

Use this pattern for bounded research or briefing work where a person has access to the relevant sources and remains accountable for the resulting claims. It supports synthesis of a supplied source set; it is not a substitute for a systematic review method.

## When to use

- Several labelled sources or research notes need thematic comparison.
- Traceability and a reviewable account of uncertainty are important.
- A knowledgeable person can inspect the original material.

Do not use when source selection itself must be systematic but no review protocol exists, when confidential material cannot be processed safely, or when nobody can verify the output.

## Inputs

- A defined research question and intended use.
- A bounded, labelled source set and any inclusion rationale.
- Relevant disclosure, privacy, copyright and assessment constraints.
- Human time to verify claims against original material.

## Workflow

1. **Human:** Define the question, purpose, audience and acceptable evidence boundaries.
2. **Human:** Select and label sources; record important exclusions or gaps.
3. **Human or AI:** Use the [identify source type skill](../../skills/identify-source-type/SKILL.md) when a source format is unclear, then confirm material classifications.
4. **AI:** Apply the [research synthesis prompt](../../prompts/research-synthesis/README.md) to organise themes, convergence, divergence and gaps from supplied material only.
5. **Human:** Compare each substantive synthesis claim with its labelled source evidence; correct overstatement, missing context and false equivalence.
6. **Human + AI:** Revise the synthesis using verified corrections while preserving unresolved uncertainty.
7. **Human:** Decide whether the output is fit for its intended use, record limitations and disclose AI assistance where required.

## Responsibilities

### Human responsibilities

- Define the question and evidence boundary.
- Select sources and judge their relevance and quality.
- Authorise any sensitive-data use.
- Verify every consequential claim and make the final fitness decision.
- Follow applicable authorship, disclosure and assessment requirements.

### AI responsibilities

- Organise supplied material without expanding the evidence set silently.
- Surface patterns, disagreement, qualifications and missing information.
- Preserve source labels and separate evidence from inference.
- Report uncertainty rather than fabricate supporting detail.

## Outputs

- A thematic synthesis suitable for human revision.
- A traceability table linking claims to supplied source labels.
- A list of disagreements, limitations and unanswered questions.
- A human verification record or annotated draft.

## Verification

The responsible person checks every substantive claim against the original source, confirms quotations and context, evaluates whether the source set supports the intended use, and records unresolved gaps. Publication-ready status is a human decision.

## Common failure modes

| Failure | Signal | Response |
| --- | --- | --- |
| Invented support | A claim has no valid supplied source label | Remove it or supply and verify relevant evidence |
| Flattened disagreement | Conflicting findings become a single consensus statement | Restore positions, conditions and strength of evidence |
| Uneven source coverage | A few sources dominate without rationale | Audit labels and rerun with explicit coverage requirements |
| Context loss | Qualifications disappear from a summarised claim | Compare with the original passage and narrow the claim |
| Unsafe data handling | Sensitive content is copied into an unsuitable tool | Stop, remove the data and use an authorised environment |

## Example

A staff member labels five policy and research sources, records that the set is illustrative rather than systematic, and asks the AI for themes and disagreement. The staff member then verifies each claim in the original sources, rejects one unsupported generalisation, adds a missing qualification and marks an unresolved evidence gap before sharing the briefing.

## Related assets

- [Research synthesis prompt](../../prompts/research-synthesis/README.md)
- [Identify source type skill](../../skills/identify-source-type/SKILL.md)
- [Prompt engineering skill](../../skills/prompt-engineering/SKILL.md)

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-24 | Initial experimental starter version. |
