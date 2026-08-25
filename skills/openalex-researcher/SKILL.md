---
name: OpenAlex researcher
type: skill
description: Discovers, maps, verifies, appraises and synthesises scholarly literature using OpenAlex as a non-exhaustive discovery and bibliometric source.
status: experimental
version: 0.1.0
maintainer: CIE and Cerebral Circuit
last_reviewed: 2026-08-25
tags:
  - research-discovery
  - literature-review
  - bibliometrics
  - source-verification
audience:
  - Researchers
  - Academic staff
  - Students
  - Curriculum designers
---

# OpenAlex Researcher

> This skill is experimental. OpenAlex is a discovery and bibliometric source, not proof of peer review, study quality or exhaustive coverage.

## Purpose

Use OpenAlex to discover and map scholarly literature, then verify and analyze the evidence needed for the user's purpose. Adapt across three pathways:

1. **Assignment research:** Find credible, relevant sources and explain how each could support the student's inquiry without writing unsupported claims.
2. **Literature review:** Run a transparent search, screening, appraisal, synthesis, and gap-analysis workflow proportionate to the requested review method.
3. **Curriculum research:** Identify trends and recommend readings aligned with learning needs, disciplinary significance, accessibility, and learner context.

Add bibliometric analysis to any pathway when it helps answer questions about volume, influence, authorship, institutions, venues, citations, collaboration, topics, or open access.

Do not store API keys in skill files or outputs. The bundled client requires `OPENALEX_API_KEY` before making any network request.

## Establish the Task

Ask only for missing information that would materially change the result. Otherwise proceed with bounded, visible assumptions.

Determine, as relevant:

- research question, topic, or curriculum need;
- intended user and decision;
- discipline, population, context, and study designs;
- date, language, geography, source-type, access, and volume constraints;
- expected output and citation style;
- curriculum outcomes, qualification level, learner profile, learning purpose, assessment connection, and workload constraints.

When curriculum context is incomplete, ask only if the omission materially affects selection. Otherwise make provisional recommendations, label assumptions, and mark unavailable criteria as unknown.

## Set the Rigour Level

Choose and label one level:

- **Exploratory search:** Use for routine assignments, initial discovery, and curriculum scans. Give a compact search summary.
- **Structured literature review:** Use explicit concepts, queries, criteria, screening, verification, appraisal, and limitations. Provide a reproducibility record.
- **Named review method:** Use terms such as *systematic review* or *scoping review* only when the requested protocol, database coverage, screening, and reporting genuinely meet the relevant methodological standard. Do not relabel an OpenAlex search as a systematic review.

Never imply that OpenAlex alone is exhaustive. Recommend additional discipline-specific databases when comprehensive coverage matters.

## Search and Discovery Workflow

1. Translate the question into concepts, synonyms, spelling variants, and exclusions. Preserve the connection between each concept and the question.
2. Search OpenAlex works broadly, then refine with dates, work types, topics, authors, institutions, sources, open-access status, or other justified filters.
3. Resolve named entities to OpenAlex IDs before filtering when possible.
4. Combine relevance-sorted results with citation-informed discovery. Avoid treating citation count as a proxy for quality; account for publication age and field differences.
5. Use backward and forward citation chasing for pivotal works when it improves coverage.
6. Deduplicate by DOI, OpenAlex ID, and normalized title. Keep versions separate when they represent materially different records or publication stages; explain the relationship.
7. Screen against explicit or inferred inclusion and exclusion criteria. Record reasons for exclusion in formal reviews.
8. Use `scripts/openalex_client.py` for repeatable, bounded searches, grouped bibliometrics, and CSV or JSON exports. It retrieves one page of at most 100 records and is not an exhaustive review tool. Consult `references/openalex_api_notes.md` when current API details are needed.

## Verify Peer Review and Metadata

Treat OpenAlex as discovery metadata, not conclusive proof of peer review or study content.

For sources retained as evidence:

1. Verify the DOI and core bibliographic metadata against Crossref or another DOI registration record, then an authoritative publisher or journal page when available.
2. Determine peer-review status from the journal or publisher, an authoritative index, or a clearly documented editorial policy. Do not infer it solely from the work type `article` or the presence of a DOI.
3. Check for retractions, expressions of concern, corrections, and material version changes using authoritative notices or recognized retraction data when relevant.
4. Preserve conflicting values when records disagree, identify each source, apply an authority hierarchy, and explain the chosen value or unresolved ambiguity.
5. Record DOI, OpenAlex ID, publication version, access route, verification sources, verification date, and confidence.
6. Flag missing or ambiguous metadata rather than inventing it.

## Analyze and Critically Appraise

Use accessible full text for claims about methods, samples, findings, limitations, or implications. If only metadata or an abstract is available:

- state the evidence boundary prominently;
- describe conclusions as abstract-reported rather than independently confirmed;
- avoid detailed risk-of-bias judgments that require full text;
- distinguish absence of reported information from evidence that it did not occur.

Select an appraisal approach appropriate to the design and purpose. At minimum, examine:

- relevance to the question and context;
- study design and fitness for the claim;
- sample, setting, measures, analysis, and limitations when available;
- risk of bias, confounding, and conflicts of interest when assessable;
- consistency or disagreement across studies;
- directness, precision, transferability, and currency;
- correction or retraction status.

Do not collapse diverse methods into a single quality score unless a justified framework requires it. Separate source credibility, methodological strength, and relevance.

## Synthesize Evidence

Organize synthesis by concepts, findings, methods, contexts, or debates rather than producing an annotated list alone.

- Distinguish evidence-supported findings from interpretation and recommendation.
- Show convergence, contradiction, uncertainty, and evidence gaps.
- Explain whether gaps reflect limited research, narrow searching, unavailable full text, or missing metadata.
- Avoid vote counting based only on whether studies report positive or negative findings.
- Generate future research questions only from demonstrated gaps and explain the basis for each.
- Provide linked citations near substantive claims and a verified reference list in the requested style; default to APA 7 for student and curriculum work when no style is specified.

## Run Bibliometric Analysis

Use OpenAlex grouping when supported and transparent local aggregation otherwise. Common analyses include publications over time; influential works, authors, institutions, sources, and topics; citation patterns and cited-by relationships; open-access availability; and authorship or institutional collaboration.

Report the query, filters, unit of analysis, counting method, time window, retrieval date, and treatment of duplicates. Interpret patterns cautiously because OpenAlex coverage, author disambiguation, topic assignment, citation accumulation, and affiliation data vary by field and time. Do not infer research quality or causal impact from bibliometric prominence.

## Recommend Curriculum Readings

Evaluate each candidate against available evidence for:

- alignment with learning outcomes and key concepts;
- learner and qualification level;
- intended learning purpose;
- connection to learning activities or assessment;
- currency and disciplinary significance;
- methodological credibility;
- accessibility, open-access status, length, complexity, and likely reading burden;
- diversity of perspectives, contexts, and authorship.

Explain why each reading belongs, what the learner should do with it, and how it connects to learning or assessment. Mark any criterion that cannot be assessed as `unknown`. Balance foundational and current readings where appropriate; do not equate recency with value.

## Produce the Right Output

Adapt or combine these deliverables:

- curated reading list with relevance and use notes;
- evidence-synthesis report;
- literature-review matrix;
- bibliometric trends report;
- curriculum-aligned reading recommendations;
- research gaps and future research questions;
- verified APA 7 or requested-style reference list;
- Markdown, CSV, or JSON structured data.

For routine searches, include a compact scope, search summary, findings, selected sources, and caveats. For formal literature reviews or research reports, include:

1. question and scope;
2. concepts, exact OpenAlex queries, filters, search date, and supplementary sources;
3. inclusion and exclusion criteria;
4. records retrieved, deduplicated, screened, included, and exclusion reasons;
5. verification and appraisal methods;
6. evidence synthesis and bibliometric methods where used;
7. limitations, uncertainty, and coverage gaps;
8. evidence matrix and verified references.

For evidence tables, include fields appropriate to the task, normally: title, year, authors, source, design, population/context, key finding, limitations, appraisal, DOI, OpenAlex ID, peer-review verification, correction status, access/full-text status, citation count, and relevance.

## Quality Gate

Before delivering:

- confirm that queries and filters match the scope;
- distinguish peer-reviewed evidence from preprints, editorials, book reviews, and other outputs;
- verify material metadata and label unresolved conflicts;
- attach claims to full text where the claim requires it;
- label abstract-only analysis clearly;
- check cited sources actually support the associated statements;
- distinguish citation influence from quality;
- disclose assumptions, missing information, and database limitations;
- ensure references and exports contain no fabricated fields;
- recommend next steps when broader databases, specialist appraisal, document access, or updated searching would materially strengthen the result.

## Version history

| Version | Date | Change |
| --- | --- | --- |
| 0.1.0 | 2026-08-25 | Imported as an experimental skill package, aligned with CIE AI Workbench metadata and updated for bounded authenticated OpenAlex use. |
