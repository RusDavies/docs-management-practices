#!/usr/bin/env python3
"""Check Markdown links and orphaned Markdown documents for this repository.

The checker is intentionally local and dependency-free. It validates:

- relative links between Markdown files
- same-file and cross-file heading anchors
- repository-local GitHub blob links
- orphaned Markdown files not reachable from README.md / DOCUMENT_MAP.md

External HTTP(S) links are deliberately not fetched; this is a structural repository
check, not a flaky network ceremony.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO_BLOB_PREFIXES = (
    "https://github.com/RusDavies/docs-management-practices/blob/master/",
    "https://github.com/RusDavies/docs-management-practices/blob/main/",
)
IGNORED_DIRS = {".git", ".venv", "node_modules", "__pycache__"}
MARKDOWN_LINK_RE = re.compile(r"(?<!!)(?:\[[^\]\n]*(?:\][^\]\n]*)*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|<((?:https?://|mailto:)[^>]+)>)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
ALLOWED_MISSING_ANCHORS = {
    # GitHub renders this generated section in the web UI for some files.
}


def iter_markdown(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(Path(dirpath, filename).relative_to(root))
    return sorted(files)


def slugify_heading(text: str) -> str:
    # Approximate GitHub's Markdown heading IDs closely enough for repo-internal links.
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9 _\-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def anchors_for(text: str) -> set[str]:
    anchors = {""}
    seen: dict[str, int] = {}
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify_heading(match.group(2))
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def extract_links(text: str) -> list[str]:
    links: list[str] = []
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1) or match.group(2)
        if not target:
            continue
        target = target.strip()
        if target.startswith(("mailto:", "tel:")):
            continue
        links.append(target)
    return links


def normalize_target(raw: str, source: Path, root: Path) -> tuple[Path | None, str, bool]:
    """Return (repo-relative path, anchor, is_external)."""
    raw = raw.strip()
    if raw.startswith("#"):
        return source, unquote(raw[1:]), False

    repo_absolute = False
    for prefix in REPO_BLOB_PREFIXES:
        if raw.startswith(prefix):
            raw = raw[len(prefix):]
            repo_absolute = True
            break
    else:
        parsed = urlparse(raw)
        if parsed.scheme in {"http", "https"}:
            return None, "", True

    parsed = urlparse(raw)
    path_part = unquote(parsed.path)
    anchor = unquote(parsed.fragment or "")

    if not path_part:
        return source, anchor, False

    if path_part.startswith("/"):
        return None, anchor, True

    target = (root / path_part).resolve() if repo_absolute else (root / source.parent / path_part).resolve()
    try:
        rel = target.relative_to(root.resolve())
    except ValueError:
        return None, anchor, True
    return rel, anchor, False


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown local links and orphaned docs.")
    parser.add_argument("--root", default=".", help="repository root; default: current directory")
    parser.add_argument(
        "--entry",
        action="append",
        default=["README.md", "DOCUMENT_MAP.md"],
        help="entry Markdown file for orphan reachability; may be repeated",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    markdown_files = iter_markdown(root)
    markdown_set = set(markdown_files)
    texts = {path: (root / path).read_text(encoding="utf-8") for path in markdown_files}
    anchors = {path: anchors_for(text) for path, text in texts.items()}

    errors: list[str] = []
    graph: dict[Path, set[Path]] = {path: set() for path in markdown_files}

    for source, text in texts.items():
        for raw_link in extract_links(text):
            target, anchor, external = normalize_target(raw_link, source, root)
            if external:
                continue
            if target is None:
                continue
            if target.suffix.lower() != ".md":
                # Local non-Markdown assets are valid if present; anchor checks do not apply.
                if not (root / target).exists():
                    errors.append(f"{source}: missing local asset link: {raw_link}")
                continue
            if target not in markdown_set:
                errors.append(f"{source}: missing Markdown link target: {raw_link}")
                continue
            graph[source].add(target)
            if anchor and slugify_heading(anchor) not in anchors[target] and anchor not in ALLOWED_MISSING_ANCHORS:
                errors.append(f"{source}: missing anchor '#{anchor}' in {target} ({raw_link})")

    entries = [Path(entry) for entry in args.entry]
    reachable: set[Path] = set()
    queue = deque(entry for entry in entries if entry in markdown_set)
    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)
        queue.extend(sorted(graph.get(current, set()) - reachable))

    orphaned = sorted(markdown_set - reachable)
    if orphaned:
        errors.append("Orphaned Markdown files not reachable from entries: " + ", ".join(str(p) for p in orphaned))

    if errors:
        print("Markdown repository check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Markdown repository check passed: {len(markdown_files)} Markdown files, "
        f"{sum(len(v) for v in graph.values())} local Markdown links, no orphan docs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
