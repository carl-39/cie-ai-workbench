---
name: Prompt engineering
type: skill
description: Designs and reviews reusable prompts with explicit inputs, outputs, constraints and verification.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-24
tags:
  - prompt-design
  - quality-assurance
audience:
  - CIE staff
  - AI capability contributors
---

# Prompt engineering

> **Starter example:** this experimental skill demonstrates the repository structure. It is not an approved CIE production asset.

## Trigger and use conditions

Use this skill when someone needs to create, revise or diagnose a prompt that will be reused across people, tasks or AI tools.

Do not use it to disguise a complex workflow as a single prompt. If success depends on several human and AI responsibilities, design a pattern or skill-supported agent instead.

## Intended outcome

A concise, ready-to-use prompt whose purpose, variable inputs, expected output, boundaries and verification requirements can be understood and tested by someone other than its author.

## Inputs

### Required

- `task`: the outcome the prompt should support.
- `users`: the people who will use the prompt.
- `context`: the information the model needs to interpret the task.
- `success-criteria`: observable characteristics of a good response.

### Optional

- `model-or-tool`: capabilities or limitations that materially affect the prompt.
- `examples`: representative inputs, outputs or known failures.
- `constraints`: format, length, evidence, privacy or process requirements.

## Workflow

1. Define the task as an outcome and identify what is outside scope.
2. Separate fixed instructions from information the user supplies each time.
3. Specify required inputs and instruct the model to flag material omissions rather than guess.
4. Describe the output structure and quality criteria without prescribing unnecessary prose.
5. Add relevant constraints, evidence rules, verification and responsible-use safeguards.
6. Remove duplicated instructions, conflicting priorities and model-specific wording that does not serve a real need.
7. Test a typical case, a sparse-input case and a case that should trigger uncertainty or refusal.
8. Revise against observed behaviour and record remaining limitations.

## Outputs

- A ready-to-use prompt.
- A short input guide.
- Expected-output and verification notes.
- Known limitations and test scenarios.

## Tools and dependencies

No specific model is required. Testing needs access to the intended AI tool or a comparable tool, plus non-sensitive representative inputs.

## Constraints

- Do not promise accuracy, determinism or capabilities the target tool does not provide.
- Do not embed personal, confidential or assessment-sensitive data in examples.
- Do not ask the model to fabricate facts, citations, access or completed actions.
- Do not replace professional or institutional judgement with confident wording.

## Quality checks

- A new user can identify every required input and where to insert it.
- The expected output can be assessed against explicit criteria.
- Missing evidence and uncertainty produce visible signals rather than invented content.
- Instructions do not conflict or repeat without purpose.
- Provider-specific assumptions are documented or removed.
- Human verification is proportionate to the consequences of error.

## Failure and uncertainty behaviour

If the task, users or success criteria are unclear, return the smallest set of questions needed before drafting. If testing reveals unstable behaviour, retain `experimental` status, document the variance and narrow the prompt rather than implying reliability.

## References and supporting resources

- [Prompt template](../../prompts/_template/README.md)
- [Quality standards](../../docs/quality-standards.md)

## Example

For a research-synthesis prompt, separate the fixed requirement to use only supplied sources from variable inputs such as the research question, source material and output length. Test whether the prompt flags unsupported claims when the supplied sources do not answer the question.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-24 | Initial experimental starter version. |
