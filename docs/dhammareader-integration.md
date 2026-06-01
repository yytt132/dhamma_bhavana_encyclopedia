# Dhamma Reader Integration Plan

The completed encyclopedia is intended to be published through the existing Dhamma Reader ecosystem.

## Public Destination

- Website: https://dhammareader.com/

Dhamma Reader is already a public Buddhist reading room. This gives the encyclopedia a prepared publication path and an audience-facing destination.

## Repository Roles

### `dhamma_bhavana_encyclopedia`

This repository is the source-of-truth for:

- Encyclopedia entries.
- Glossary entries.
- Comparison essays.
- Concept dossiers.
- Source metadata.
- JSON schemas.
- Editorial workflow.
- Validation and copyright-safety policy.

### Dhamma Reader website

Dhamma Reader is the intended public integration surface for:

- User-facing encyclopedia pages.
- Search and navigation.
- Links from reading-room content to encyclopedia entries.
- Public release of reviewed Korean-language practice materials.

## Integration Principles

- Only `reviewed` or `published` entries should be exported to the public site.
- Draft entries can remain visible in the source repository but should be clearly marked.
- Source metadata should be visible without exposing copyrighted source text.
- Korean-language accessibility is the default user experience.
- English summaries and mission text should remain available for international contributors and reviewers.

## Proposed Export Shape

Reviewed content can be exported as:

```text
entry_id
title
title_ko
entry_type
status
summary
body
related_entries
sources
updated_at
```

## Near-Term Tasks

- Define export format for reviewed entries.
- Add a script that lists public-ready entries.
- Add source metadata mapping for Dhamma Reader.
- Add search index preparation.
- Add links from Dhamma Reader topic pages to encyclopedia entries.
