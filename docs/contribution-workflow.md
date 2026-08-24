# Contribution workflow

## Lifecycle

`Draft → Review → Test → Approve → Publish → Monitor → Revise/Deprecate`

| Stage | Practical meaning |
| --- | --- |
| Draft | A need, owner and initial asset are documented. Status is `experimental`. |
| Review | A peer checks clarity, boundaries, risks and duplication. |
| Test | Representative and adverse cases are run; results and limitations are recorded. Status may move to `testing`. |
| Approve | The designated CIE reviewer confirms intended use. Status becomes `approved`. This role is still to be named. |
| Publish | The reviewed asset is merged and visible in the catalogue. |
| Monitor | Users report failures, changed assumptions and model/tool drift. |
| Revise/Deprecate | The asset is improved with a version note or marked `deprecated` with a replacement where available. |

## Pull requests

Use a short-lived branch and the pull-request template. Review should be proportional: a wording correction needs less evidence than an agent that can act on institutional data. At least one reviewer other than the author should review substantive assets. Shared CIE/Cerebral Circuit assets should have review representation from both parties until ownership rules are agreed.

The pull request should state:

- the problem and intended users;
- what changed and which assets are affected;
- test cases, results and known failures;
- privacy, educational and organisational risks;
- verification and human-confirmation points;
- maintainer and proposed status;
- any unresolved decision.

## Status changes

Status changes require evidence in the pull request. `approved` means approved for the scope stated in the asset, not universally safe. Deprecation should preserve the asset, explain why it should no longer be used and link to a replacement if one exists.
