---
name: Verified research synthesis
type: pattern
description: Uses AI for structured synthesis while a person controls source selection, verification and consequential interpretation.
tags: [research, synthesis, verification, workflow]
audience: [education professionals, researchers]
status: experimental
version: 0.1.0
maintainer: CIE / unassigned
last_reviewed: 2026-08-24
---

# Verified research synthesis

## Problem

AI can organise a large set of notes quickly, but fluent synthesis can obscure weak evidence, source disagreement or fabricated details.

## Context and when to use

Use for an evidence brief or exploratory review when a person can select and access the source set. Do not use it as a substitute for a systematic-review protocol, specialist appraisal or independent verification in high-stakes decisions.

## Responsibilities

| Human responsibilities | AI responsibilities |
| --- | --- |
| Define the question and inclusion boundaries | Structure supplied material around the question |
| Select, label and retain original sources | Link claims to source labels |
| Judge source quality and materiality | Surface convergence, disagreement, gaps and uncertainty |
| Verify claims and decide implications | Revise the synthesis after corrections |

## Inputs and outputs

Inputs are a question, audience, labelled notes, original sources and desired format. Outputs are a draft synthesis, claim-to-source trace, uncertainty/gap list and a verified final version.

## Workflow

1. The human defines the question, scope and intended decision.
2. The human gathers sources, records provenance and labels notes.
3. AI produces a bounded synthesis using the [research synthesis prompt](../../prompts/research-synthesis/).
4. The human samples every material claim against its original source and checks all quotations, figures and citations.
5. AI revises only from documented corrections and identifies remaining uncertainty.
6. The responsible human approves interpretation and use, or narrows the conclusion.

## Verification

Verify all claims that affect the conclusion, all direct quotations, numerical findings and bibliographic details. For consequential work, use a second reviewer or domain specialist proportional to the risk.

## Common failure modes

| Failure mode | Detection or response |
| --- | --- |
| Unsupported bridge claim | Require a source label or mark it as inference |
| Disagreement flattened into consensus | Compare each theme against individual source notes |
| Weak source treated as decisive | Add explicit source appraisal by a person |
| Correct citation attached to wrong claim | Check claim meaning in the original context |
| Sensitive data copied into a model | Minimise or de-identify data and use an authorised environment |

## Example

For a briefing on AI literacy, the researcher selects current studies and policy documents, labels extracted notes, uses AI to group findings and then checks every practical recommendation against the source record before circulation.

## Related assets

- [Research synthesis prompt](../../prompts/research-synthesis/)
- [Source type identification skill](../../skills/source-type-identification/)
