# Architecture

## Design intent

The repository is human-readable first and machine-readable where this provides practical value. Each asset lives in a stable kebab-case directory with one primary Markdown file and lightweight YAML front matter. A human-maintained catalogue supports browsing now; the same metadata can support a future search interface or agent.

## Asset boundaries

- **Prompt:** portable instructions and an expected response contract.
- **Skill:** a reusable method with workflow, constraints and quality checks. A skill may contain prompts but is not reducible to them.
- **Agent:** a bounded operating role that invokes skills and tools against named sources of truth. Authority and confirmation points are explicit.
- **Pattern:** an end-to-end human–AI arrangement describing responsibilities, verification and failure modes.

References should use relative links. Assets may point to other assets, but copying their contents should be avoided. Agents list skills by stable repository path. Patterns link to the prompts, skills or agents they use.

## Standard asset shape

```text
<type>/<asset-name>/
├── README.md or SKILL.md
├── CHANGELOG.md        # recommended after the first substantive revision
├── examples/           # optional
├── references/         # optional, only when needed
└── tests/              # optional evaluations or test cases
```

Skills use `SKILL.md` to remain compatible with ChatGPT/Codex-style packaging. Other assets use `README.md`. Do not add empty directories or support files merely to satisfy this illustrative shape.

## Metadata

The common required fields are `name`, `type`, `description`, `status`, `version`, `maintainer` and `last_reviewed`. `tags` and `audience` improve discovery and are recommended. Type-specific content remains in the Markdown body rather than a large metadata record.

The catalogue is deliberately manual at first. If volume makes it unreliable, a generated index can replace it while retaining a readable Markdown output.

## Future interfaces

A future Workbench interface can parse front matter, filter by maturity and audience, and guide users to an appropriate capability. Such an interface must continue to show limitations, status and verification requirements rather than presenting all assets as interchangeable or approved.
