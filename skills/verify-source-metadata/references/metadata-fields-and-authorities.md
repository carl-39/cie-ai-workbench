# Metadata fields and authority routing

Use this reference to choose an adaptive schema and verification route. Include only applicable fields, but retain additional meaningful fields found in the source.

## Shared fields

- Source type and subtype
- Work title, subtitle, translated title, and part title or number
- Creators, editors, translators, directors, presenters, producers, compilers, and other contributors with roles
- Publication, release, upload, defence, acceptance, update, and access dates where relevant
- Language and script
- Edition, revision, version, status, format, and medium
- Publisher, issuing organisation, institution, platform, repository, or distributor
- Persistent and standard identifiers: DOI, ISBN, ISSN, eISSN, handle, URN, accession number, repository ID, video ID, dataset ID, and canonical URL

## Source-specific fields

### Journal articles

Capture journal title, volume, issue, supplement, article number, page range, publication dates, DOI, ISSNs, publisher, article status, and version.

Prioritise DOI registration agency record, publisher or journal landing page, trusted scholarly index, then library catalogue.

### Books

Capture edition, volume, series and number, publisher, publication place when the record itself treats it as meaningful, publication date, ISBNs by format, DOI, editors, translators, and format.

Prioritise publisher and ISBN or national bibliographic records, then national or university library catalogues and trusted union catalogues. Distinguish hardback, paperback, ebook, revised editions, and translations.

### Book chapters and reference entries

Capture chapter or entry title, chapter authors, book title, book editors, edition, volume, page range, publisher, date, chapter DOI, book DOI, and ISBNs.

Prioritise chapter DOI record and publisher page, then the book record and library catalogues. Do not substitute book-level metadata for chapter-level metadata without labelling it.

### Reports and policy documents

Capture personal and corporate authors, report or series number, version, issuing body, department, place if meaningful, publication date, DOI or institutional identifier, and canonical URL.

Prioritise the issuing organisation's record and document, DOI or repository record, then national or institutional catalogues. Distinguish drafts, consultation papers, final reports, summaries, and revised policies.

### Theses and dissertations

Capture author, title, award type, discipline or department when stated, degree-granting institution, award or publication year, repository, handle or DOI, and publication status.

Prioritise the awarding institution's repository and catalogue, then national thesis services, DOI record, and trusted union catalogues. Distinguish the examined thesis from later articles or books.

### Conference works

Capture contribution title, authors, conference title, dates and location, proceedings title, editors, publisher or organiser, pages or article number, presentation type, DOI, ISBN or ISSN, and version.

Prioritise DOI record, proceedings publisher, and official conference or institutional repository record. Distinguish abstract, poster, presentation, preprint, and full proceedings paper.

### Webpages and online publications

Capture page or post title, site or publication title, personal or corporate author, publication and update dates, publisher or owner, canonical URL, version, and content type.

Prioritise the canonical page and site's own structured metadata, then the responsible organisation's record and reputable web archives. Treat an archive snapshot as a distinct manifestation when content or date differs.

### Videos, including YouTube

Capture video title, uploader or channel, responsible creator roles where supported, platform, upload or release date, duration when bibliographically useful, video ID, canonical URL, series or playlist when relevant, language, and version or live-recording status.

Prioritise the canonical platform record and verified creator or issuing organisation page. Use platform APIs or embedded structured metadata when available. Do not equate the uploader with the work's creator unless evidence supports that role.

### Podcasts and audio

Capture episode title and number, podcast or series title, hosts, guests and creators with roles, publisher or network, release date, season, duration when useful, platform identifier, and canonical URL.

Prioritise the publisher or podcast's canonical feed and episode page, then the responsible network and platform record.

### Datasets and software

Capture title, creators, publisher or repository, release date, version, resource type, DOI or persistent identifier, licence, and related publication or project identifiers.

Prioritise DataCite or another identifier registration record and the canonical repository record. Keep versions and releases separate.

### Other or ambiguous sources

Describe the object's defining characteristics, select the closest schema without forcing a false type, and capture all persistent identifiers and provenance. State what evidence would establish the type or identity more confidently.

## Confidence guide

- **High:** Strong persistent identifier or exact authoritative record; identity and version align; key fields agree.
- **Medium:** Probable identity supported by an authoritative record, but a key field, version, or contributor role is incomplete or conflicting.
- **Low:** Only partial or secondary evidence; several plausible records; identity, version, or key fields remain unresolved.
