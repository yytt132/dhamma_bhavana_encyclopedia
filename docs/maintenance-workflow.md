# Maintenance Workflow

This document defines the expected maintenance workflow.

## Weekly Triage

Review open issues and classify them:

- `entry`
- `glossary`
- `comparison`
- `source metadata`
- `editorial review`
- `copyright`
- `schema`
- `website`
- `good first issue`
- `help wanted`

## Pull Request Review

Check:

- Does the PR add copyrighted source text?
- Do content files include required front matter?
- Are statuses realistic?
- Are source IDs present?
- Are related entries listed?
- Does validation pass?
- Is human review needed before publication?

## Entry Publication Workflow

1. `stub`: create initial structure.
2. `draft`: add prose or AI-assisted first draft.
3. `sourced`: add source metadata and claim categories.
4. `reviewed`: human editorial or subject review.
5. `published`: stable public entry.

## Release Workflow

1. Update `CHANGELOG.md`.
2. Run validation.
3. Create a version tag.
4. Push the tag.
5. Publish release notes on GitHub.

## AI-Assisted Maintenance

AI tools can help with:

- issue triage
- PR summaries
- schema migration
- validation fixes
- entry outline drafts
- release note drafts

AI output should not be treated as final scholarly authority. Publication-quality entries require human review.
