# OpenAlex API Notes

## Documentation index

The OpenAlex LLM documentation index is available at `https://developers.openalex.org/llms.txt`. Consult it when a task needs current endpoint details beyond this skill's core workflow.

## Key details

- Base URL: `https://api.openalex.org`.
- API key parameter: `api_key`.
- Singleton calls such as `/works/W2741809807` are free.
- List and search calls may have usage costs depending on OpenAlex account terms.
- `per_page` maximum is 100.
- Use cursor pagination for deep result sets.

## Bundled client boundaries

- Set `OPENALEX_API_KEY` before running `scripts/openalex_client.py`; the client refuses all network requests without it.
- The client performs at most three attempts for rate-limit or transient server failures and never prints or stores the key.
- `search-works` exports one result page only, with a maximum of 100 records. Treat the output as bounded discovery, not an exhaustive search or systematic-review dataset.
- Review current OpenAlex pricing and response metadata before large or repeated queries. Use cursor pagination only through a separately reviewed workflow that makes retrieval volume and cost explicit.

## Entity prefixes

| Prefix | Entity |
|---|---|
| W | Work |
| A | Author |
| S | Source |
| I | Institution |
| T | Topic |
| K | Keyword |
| P | Publisher |
| F | Funder |

## External IDs

Examples:

- DOI work lookup: `/works/doi:10.7717/peerj.4375`
- PMID work lookup: `/works/pmid:29456894`
- ORCID author lookup: `/authors/https://orcid.org/0000-0001-6187-6610`
- ROR institution lookup: `/institutions/https://ror.org/02y3ad647`
- ISSN source lookup: `/sources/issn:0028-0836`

## Common group_by fields

- `publication_year`
- `type`
- `is_oa`
- `topics.id`
- `authorships.author.id`
- `authorships.institutions.id`
- `primary_location.source.id`
- `primary_location.source.publisher_lineage`
