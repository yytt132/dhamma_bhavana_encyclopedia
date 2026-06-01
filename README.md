# Dhamma Bhavana Encyclopedia

An open-source, source-aware encyclopedia of Buddhist and contemplative practice.

This project combines:

- SEP-style scholarly essays for major concepts.
- Princeton/DDB-style lexical entries for Buddhist terms.
- A source-aware ontology of practices, methods, traditions, goals, body models, and claims.
- Editorial workflows for human-reviewed AI-assisted scholarship.

The goal is not to collapse all contemplative practices into one universal vocabulary. The project preserves tradition, lineage, language, method, goal, authority structure, and evidence status for each claim.

## Korean Summary

**Dhamma Bhavana Encyclopedia**는 불교와 명상·수행 전통을 출처 기반으로 정리하는 오픈소스 백과 프로젝트입니다.

SEP식 소논문, 불교 전문 사전식 용어 항목, 수행 온톨로지, 문헌 기반 주석 체계를 결합합니다. 최종 목표는 각 핵심 개념마다 신뢰 가능한 소논문형 항목을 만들고, 관련 용어·수행법·원전·비교 항목을 서로 연결하는 것입니다.

## Project Scope

The project contains several types of public material:

- `content/entries`: long-form encyclopedia essays.
- `content/glossary`: shorter lexical entries.
- `content/comparisons`: comparative essays and matrices.
- `content/dossiers`: structured research notes used before essay drafting.
- `data/public`: public metadata and sample datasets.
- `packages/schema`: JSON schemas for entries, sources, dossiers, and claims.
- `docs`: editorial, copyright, and contribution guides.

The project does **not** publish copyrighted PDFs, OCR text, extracted book chapters, or long verbatim practice instructions from copyrighted sources.

## Entry Status

Every entry should declare a review status:

- `stub`: placeholder structure only.
- `draft`: early human or AI-assisted draft.
- `sourced`: claims have source metadata.
- `reviewed`: reviewed by an editor or subject reviewer.
- `published`: stable public version.
- `needs-work`: known issues remain.

## Initial Roadmap

### v0.1

- Public repo scaffold.
- Licensing and contribution policy.
- Editorial guide.
- Copyright policy.
- Core schemas.
- Sample dossier and sample SEP-style entry.

### v0.2

- Static website shell.
- Entry page renderer.
- Search index prototype.
- Related-entry graph.
- Review-status badges.

### v0.3

- First 25 core concept entries.
- First 25 glossary entries.
- First 10 comparison essays.
- Public source metadata index.

## Suggested First Core Entries

- `bhavana`
- `sati`
- `samatha`
- `vipassana`
- `samadhi`
- `dhyana-jhana`
- `metta`
- `karuna`
- `sunyata`
- `zazen`
- `pranayama`
- `tonglen`

## License

- Code: MIT License. See `LICENSE`.
- Original encyclopedia content: CC BY-SA 4.0. See `LICENSE-CONTENT.md`.
- Public metadata and schemas: CC BY 4.0 unless a file says otherwise.

Third-party sources remain under their own licenses. Do not add copyrighted PDFs, OCR dumps, or long extracted passages to this repository.

