from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_ENTRY_TYPES = {"concept", "practice", "lexical", "tradition", "comparison", "source"}
ALLOWED_STATUSES = {"stub", "draft", "sourced", "reviewed", "published", "needs-work"}
FORBIDDEN_EXTENSIONS = {".pdf", ".epub", ".mobi", ".azw3", ".djvu"}

REQUIRED_DOCS = [
    "README.md",
    "LICENSE",
    "LICENSE-CONTENT.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "docs/mission-ko.md",
    "docs/mission-en.md",
    "docs/editorial-guide.md",
    "docs/copyright-policy.md",
    "docs/dhammareader-integration.md",
    "docs/founder-statement-ko.md",
    "docs/founder-statement-en.md",
]

REQUIRED_SCHEMAS = [
    "packages/schema/entry.schema.json",
    "packages/schema/dossier.schema.json",
    "packages/schema/source.schema.json",
    "packages/schema/claim.schema.json",
]

REQUIRED_FRONTMATTER_KEYS = {
    "id",
    "title",
    "entry_type",
    "status",
    "summary",
    "related_entries",
    "sources",
    "license",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARNING: {message}")


def parse_json_files() -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def check_required_files() -> None:
    for rel in REQUIRED_DOCS + REQUIRED_SCHEMAS:
        if not (ROOT / rel).exists():
            fail(f"Missing required file: {rel}")


def check_forbidden_files() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            fail(f"Forbidden source/corpus file is tracked or present: {path.relative_to(ROOT)}")


def parse_frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"Missing front matter fence in {path.relative_to(ROOT)}")

    end = None
    for idx, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = idx
            break
    if end is None:
        fail(f"Unclosed front matter in {path.relative_to(ROOT)}")

    data: dict[str, object] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        line = raw.rstrip()
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            key, value = match.group(1), match.group(2).strip()
            if value == "":
                data[key] = []
                current_key = key
            else:
                data[key] = value.strip("\"'")
                current_key = None
            continue
        stripped = line.strip()
        if stripped.startswith("- ") and current_key:
            data.setdefault(current_key, [])
            assert isinstance(data[current_key], list)
            data[current_key].append(stripped[2:].strip().strip("\"'"))

    return data


def source_ids() -> set[str]:
    sample = ROOT / "data/public/sources.sample.json"
    if not sample.exists():
        return set()
    data = json.loads(sample.read_text(encoding="utf-8"))
    return {item["id"] for item in data if isinstance(item, dict) and "id" in item}


def check_content_frontmatter() -> None:
    known_sources = source_ids()
    content_dirs = [ROOT / "content/entries", ROOT / "content/glossary", ROOT / "content/comparisons"]

    for directory in content_dirs:
        if not directory.exists():
            continue
        for path in sorted(list(directory.glob("*.md")) + list(directory.glob("*.mdx"))):
            data = parse_frontmatter(path)
            missing = REQUIRED_FRONTMATTER_KEYS - data.keys()
            if missing:
                fail(f"{path.relative_to(ROOT)} missing front matter keys: {sorted(missing)}")

            entry_type = str(data["entry_type"])
            status = str(data["status"])
            if entry_type not in ALLOWED_ENTRY_TYPES:
                fail(f"{path.relative_to(ROOT)} has invalid entry_type: {entry_type}")
            if status not in ALLOWED_STATUSES:
                fail(f"{path.relative_to(ROOT)} has invalid status: {status}")

            entry_id = str(data["id"])
            if entry_id != path.stem:
                warn(f"{path.relative_to(ROOT)} id does not match filename stem: {entry_id}")

            sources = data.get("sources", [])
            if isinstance(sources, list):
                for source in sources:
                    if known_sources and source not in known_sources:
                        warn(f"{path.relative_to(ROOT)} references unknown source id: {source}")
            else:
                fail(f"{path.relative_to(ROOT)} sources must be a list")


def check_mission_links() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for expected in [
        "docs/mission-en.md",
        "docs/founder-statement-ko.md",
        "docs/dhammareader-integration.md",
        "docs/core-entry-roadmap.md",
    ]:
        if expected not in readme:
            fail(f"README.md should link to {expected}")


def main() -> None:
    check_required_files()
    parse_json_files()
    check_forbidden_files()
    check_content_frontmatter()
    check_mission_links()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
