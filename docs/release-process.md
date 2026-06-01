# Release Process

The project uses lightweight semantic versioning.

## Version Meaning

- `0.1.x`: repository foundation and policy.
- `0.2.x`: website prototype.
- `0.3.x`: first public content corpus.
- `0.4.x`: review workflow and stronger automation.

## Release Checklist

- [ ] Validation passes.
- [ ] `CHANGELOG.md` is updated.
- [ ] Roadmap status is current.
- [ ] Copyright-risk files are not tracked.
- [ ] New schemas and examples are documented.
- [ ] Release tag is pushed.

## Creating a Release

```powershell
git status --short
python scripts/validate_repository.py
git tag v0.1.0
git push origin v0.1.0
```

Then create GitHub release notes from `CHANGELOG.md`.
