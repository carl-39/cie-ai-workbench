---
name: prompt-engineering
type: skill
description: Designs, critiques and tests reusable prompts against a defined task, audience and output contract.
tags: [prompts, design, testing]
audience: [AI capability authors, education professionals]
status: experimental
version: 0.1.0
maintainer: CIE / unassigned
last_reviewed: 2026-08-24
---

# Prompt engineering

## Intended outcome

A reusable prompt whose purpose, inputs, boundaries, expected output and verification requirements are clear enough to test. The skill improves instructions; it does not guarantee factual correctness or safe deployment.

## Trigger and use conditions

Use when creating, repairing or standardising a prompt intended for repeated use. Do not use a single elaborate prompt to conceal a multi-stage capability that needs a skill, agent or human–AI pattern.

## Workflow

1. Define the user, recurring problem, decision context and acceptable output.
2. Identify required inputs, optional context, missing-information behaviour and tool assumptions.
3. Separate task instructions from evidence, examples and output format.
4. Add boundaries: prohibited fabrication, uncertainty behaviour, privacy and confirmation requirements.
5. Draft the shortest instruction set that preserves the necessary controls.
6. Test a normal case, an incomplete-input case and an ambiguous or adversarial case.
7. Revise instructions based on observable failures; document limitations rather than hiding them with more wording.
8. Package using the prompt template and hand off for domain review.

## Inputs and outputs

Inputs include the current prompt if one exists, intended users, use cases, model/tool context, examples and success criteria. Output is a ready-to-use prompt with concise usage guidance, assumptions, limitations and a test record or test plan.

## Constraints

- Do not invent institutional rules, sources or tool abilities.
- Preserve the requested professional method rather than optimising only for fluent output.
- Keep portable instructions vendor-neutral; isolate provider-specific syntax.
- Require human review for consequential decisions.

## Quality checks

- A user can identify what to supply and what will be returned.
- Each instruction contributes to the task, control or output contract.
- Missing or conflicting information produces a defined response.
- Tests can distinguish success from merely plausible prose.
- Verification and privacy requirements are visible.

## Failure and uncertainty behaviour

Ask for missing information only when it materially changes the prompt. Otherwise state assumptions and proceed. If the underlying task lacks a defensible method or grants unsafe authority, flag that design problem rather than encoding it.

## Example

For a research-synthesis prompt, test faithful synthesis, contradictory sources and notes without source labels. Check claim traceability and whether uncertainty survives compression.
