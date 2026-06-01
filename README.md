# Dhamma Bhavana Encyclopedia

[![Validate repository](https://github.com/yytt132/dhamma_bhavana_encyclopedia/actions/workflows/validate.yml/badge.svg)](https://github.com/yytt132/dhamma_bhavana_encyclopedia/actions/workflows/validate.yml)
[![Code License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY-SA 4.0](https://img.shields.io/badge/content-CC%20BY--SA%204.0-green.svg)](LICENSE-CONTENT.md)
[![Project status: v0.1 foundation](https://img.shields.io/badge/status-v0.1%20foundation-yellow.svg)](docs/roadmap.md)

An open-source, source-aware encyclopedia of Buddhist and contemplative practice.

## Reviewer Quick Links

- Mission, Korean: [`docs/mission-ko.md`](docs/mission-ko.md)
- Mission, English: [`docs/mission-en.md`](docs/mission-en.md)
- Why this project matters: [`docs/openai-oss-application.md`](docs/openai-oss-application.md)
- API credit plan: [`docs/api-credit-plan.md`](docs/api-credit-plan.md)
- Deployment target: [`docs/dhammareader-integration.md`](docs/dhammareader-integration.md)
- Core entry roadmap: [`docs/core-entry-roadmap.md`](docs/core-entry-roadmap.md)
- Initial backlog: [`docs/initial-backlog.md`](docs/initial-backlog.md)
- Editorial guide: [`docs/editorial-guide.md`](docs/editorial-guide.md)
- Copyright policy: [`docs/copyright-policy.md`](docs/copyright-policy.md)
- Governance: [`GOVERNANCE.md`](GOVERNANCE.md)
- Maintenance workflow: [`docs/maintenance-workflow.md`](docs/maintenance-workflow.md)

## Why This Exists

English-speaking Buddhist practitioners and researchers already have access to many strong reference ecosystems: the Stanford Encyclopedia of Philosophy, the Digital Dictionary of Buddhism, the Princeton Dictionary of Buddhism, SuttaCentral, 84000, and other scholarly or practice-oriented resources.

Korean-speaking practitioners do not yet have an open, reliable, practice-oriented encyclopedia of comparable usefulness. There are important Buddhist dictionaries and reference works, but there is still a gap for Korean meditators, dharma teachers, meditation instructors, and serious beginners who need clear, source-aware, accessible explanations of practice concepts.

This project exists to help fill that gap.

한국어를 사용하는 수행자, 명상지도사, 불교 공부를 시작하는 사람, 그리고 더 깊이 수행론을 이해하고 싶은 사람들을 위해 공개적인 수행 백과를 만드는 것이 이 프로젝트의 이유입니다.

This project combines:

- SEP-style scholarly essays for major concepts.
- Princeton/DDB-style lexical entries for Buddhist terms.
- A source-aware ontology of practices, methods, traditions, goals, body models, and claims.
- Editorial workflows for human-reviewed AI-assisted scholarship.

The goal is not to collapse all contemplative practices into one universal vocabulary. The project preserves tradition, lineage, language, method, goal, authority structure, and evidence status for each claim.

## Current Repository Status

This repository is in the `v0.1 public foundation` phase.

It already includes:

- Open-source license and separate content license.
- Korean and English mission statements.
- Editorial, copyright, contribution, governance, and support policies.
- JSON schemas for entries, dossiers, source metadata, and source-aware claims.
- Sample SEP-style entry, glossary entry, comparison entry, and concept dossiers.
- GitHub issue templates, PR template, CODEOWNERS, and validation workflow.
- A local validation script for JSON, content front matter, required docs, and repository safety checks.

The next milestone is `v0.2 website prototype`: a static public site, search index, entry renderer, and review-status display.

## Public Deployment Path

The completed encyclopedia is intended to be published through the existing Dhamma Reader ecosystem:

- Public site: [dhammareader.com](https://dhammareader.com/)
- Deployment repository: [yytt132/dhammareader](https://github.com/yytt132/dhammareader)

This repository focuses on open encyclopedia content, schemas, editorial workflow, and validation. The Dhamma Reader repository and domain provide the prepared public reading environment where reviewed encyclopedia content can later be integrated.

## Korean Summary

**Dhamma Bhavana Encyclopedia**는 불교와 명상·수행 전통을 출처 기반으로 정리하는 오픈소스 백과 프로젝트입니다.

SEP식 소논문, 불교 전문 사전식 용어 항목, 수행 온톨로지, 문헌 기반 주석 체계를 결합합니다. 최종 목표는 각 핵심 개념마다 신뢰 가능한 소논문형 항목을 만들고, 관련 용어·수행법·원전·비교 항목을 서로 연결하는 것입니다.

자세한 한국어 사명문은 `docs/mission-ko.md`를 보세요.

For the full English mission statement, see `docs/mission-en.md`.

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

See the full roadmap in [`docs/roadmap.md`](docs/roadmap.md).

## OpenAI Codex OSS Support Fit

This project is a strong fit for maintainer tooling because it requires continuous issue triage, source metadata normalization, schema validation, article drafting, cross-reference review, release workflow management, and copyright-safety checks.

Codex would be used to help maintain an open Korean-language knowledge base for Buddhist and contemplative practice, while keeping final interpretation and publication decisions under human review.

See [`docs/openai-oss-application.md`](docs/openai-oss-application.md) and [`docs/api-credit-plan.md`](docs/api-credit-plan.md).

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
