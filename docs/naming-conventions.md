# Naming conventions

## Directories and identifiers

- Use lowercase kebab-case: `source-type-identification`.
- Prefer a descriptive capability or outcome over a team name or tool name.
- Treat the repository-relative path as the stable identifier.
- Keep versions in front matter and changelogs, never in names such as `assessment-design-v7-final`.
- Avoid abbreviations unless they are well established for the intended users.

Examples:

```text
skills/prompt-engineering/
skills/assessment-design/
prompts/critique-assessment-brief/
prompts/synthesise-research-notes/
agents/apa-7-assistant/
patterns/verified-research-synthesis/
```

## Files

- Use `SKILL.md` as the primary skill file.
- Use `README.md` as the primary file for prompts, agents and patterns.
- Use `CHANGELOG.md` for meaningful version history.
- Use descriptive kebab-case filenames for supporting material.

## Versions and dates

Use semantic versions where useful: `0.1.0` for an initial experimental asset, `1.0.0` for an approved stable contract and increment major versions for incompatible changes. Dates use ISO 8601: `YYYY-MM-DD`.
