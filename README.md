# CIE AI Workbench

> **CIE AI Workbench** is a shared library of reusable prompts, skills, agents and human–AI workflow patterns for educational and organisational work.

The Workbench is developed by the Centre for Innovation in Education (CIE) in partnership with Cerebral Circuit. It provides a structured source of truth for AI capabilities worth using again, improving and maintaining. It is not merely a prompt library.

## What belongs here

| Asset | What it captures | Start here |
| --- | --- | --- |
| Prompt | Reusable instructions for a model or AI tool | [`prompts/`](prompts/) |
| Skill | A specialist method or workflow with quality controls | [`skills/`](skills/) |
| Agent | A bounded role combining instructions, skills, knowledge and tools | [`agents/`](agents/) |
| Pattern | A proven division of work between people and AI | [`patterns/`](patterns/) |

A prompt tells a tool what to do. A skill describes how to perform a capability reliably. An agent applies selected capabilities within explicit authority and risk limits. A pattern documents the wider human–AI practice in which one or more assets may be used.

## Browse and use

1. Browse [collections](collections/README.md) by project or function, use [`CATALOGUE.md`](CATALOGUE.md), or open an asset-type directory.
2. Check the asset's status, intended audience, assumptions and limitations.
3. Use only assets whose approved scope matches the intended task.
4. Follow the stated verification and human-oversight requirements.
5. Record useful test findings or propose an improvement through an issue or pull request.

## Contribute

Create a descriptive, lowercase, kebab-case directory under the appropriate asset type. Copy its `_template`, complete only the relevant sections and add its metadata to [`CATALOGUE.md`](CATALOGUE.md). Contributions move through:

`Draft → Review → Test → Approve → Publish → Monitor → Revise/Deprecate`

See [`CONTRIBUTING.md`](CONTRIBUTING.md), the [contribution workflow](docs/contribution-workflow.md) and [quality standards](docs/quality-standards.md). Pull requests should explain the need, evidence of testing, risks, limitations and ownership.

## Quality and responsible use

Important assets need explicit success criteria, representative tests, version history and a named maintainer. Factual claims must be checked against appropriate sources. Consequential educational or organisational decisions remain subject to human judgement. Do not include confidential, personal or sensitive data unless its use is authorised and protected.

Assets should remain vendor-flexible where possible. Model or tool dependencies belong in the asset documentation rather than being assumed. Versions are recorded in metadata and changelogs, not filenames.

## Repository map

- [`collections/`](collections/): project- and function-based routes through related canonical assets
- [`docs/architecture.md`](docs/architecture.md): design and relationships
- [`docs/naming-conventions.md`](docs/naming-conventions.md): names and identifiers
- [`docs/contribution-workflow.md`](docs/contribution-workflow.md): lifecycle and pull requests
- [`docs/quality-standards.md`](docs/quality-standards.md): review framework
- [`schemas/`](schemas/): lightweight metadata definition

## Licence

No open-source licence has yet been selected. See [`LICENSE`](LICENSE). CIE and Cerebral Circuit should confirm ownership, reuse permissions and the intended public/private status before external distribution.
