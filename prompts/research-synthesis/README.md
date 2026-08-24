---
name: Research synthesis
type: prompt
description: Synthesises supplied research notes into a traceable account of findings, disagreements and gaps.
tags: [research, synthesis, evidence]
audience: [education professionals, researchers]
status: experimental
version: 0.1.0
maintainer: CIE / unassigned
last_reviewed: 2026-08-24
---

# Research synthesis

## Purpose

Produce a concise synthesis of supplied research material without inventing evidence or flattening disagreement. This prompt does not independently verify sources unless source access and a verification step are explicitly provided.

## Ready-to-use prompt

```text
Synthesise the supplied research notes for the stated audience and question.

1. Use only the supplied material unless I explicitly authorise outside research.
2. Identify the main answer, areas of convergence, material disagreements,
   limitations and unanswered questions.
3. Link each substantive claim to the supplied source label. Do not invent
   citations, quotations, findings or author intent.
4. Distinguish source claims from your inference. If the evidence is
   insufficient, say so.
5. Preserve qualifications that affect interpretation. Do not treat frequency
   of mention as strength of evidence.
6. End with practical implications that follow from the evidence and a short
   list of claims requiring verification before consequential use.

Question: [QUESTION]
Audience: [AUDIENCE]
Desired length or format: [FORMAT]
Source-labelled notes: [NOTES]
```

## Inputs and expected output

Required inputs are a question, audience and source-labelled notes. An optional format or length may be supplied. The output should contain a bottom line, thematic synthesis, disagreements or gaps, evidence-bounded implications and verification list.

## Assumptions and limitations

Quality depends on the completeness and accuracy of the supplied notes. The prompt cannot establish source quality, detect omitted evidence or verify citations without source access.

## Verification and responsible use

Check material claims against the original sources before publication, policy, assessment or other consequential use. Remove personal or confidential data from notes unless authorised handling is available.
