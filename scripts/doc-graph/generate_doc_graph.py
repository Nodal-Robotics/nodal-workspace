#!/usr/bin/env python3

import os
import re
import sys
import yaml
from collections import defaultdict

DOCS_DIR = "docs"
OUTPUT_MD = "docs/navigation-map.md"

FRONTMATTER_RE = re.compile(r"^---\s*(.*?)\s*---", re.DOTALL)

REQUIRED_FIELDS = ["title", "nav_order"]
OPTIONAL_FIELDS = ["parent", "permalink", "status"]

ALLOWED_STATUS = {"draft", "normative", "informative"}


class DocPage:
    def __init__(self, path, meta):
        self.path = path
        self.title = meta["title"]
        self.nav_order = meta["nav_order"]
        self.parent = meta.get("parent")
        self.permalink = meta.get("permalink")
        self.status = meta.get("status")


def error(msg):
    print(f"❌ ERROR: {msg}")
    sys.exit(1)


def parse_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    match = FRONTMATTER_RE.match(content)
    if not match:
        error(f"Missing frontmatter in {filepath}")

    try:
        meta = yaml.safe_load(match.group(1))
    except Exception as e:
        error(f"Invalid YAML in {filepath}: {e}")

    for field in REQUIRED_FIELDS:
        if field not in meta:
            error(f"Missing '{field}' in {filepath}")

    if not isinstance(meta["nav_order"], int) or meta["nav_order"] <= 0:
        error(f"Invalid nav_order in {filepath}")

    if "status" in meta and meta["status"] not in ALLOWED_STATUS:
        error(f"Invalid status '{meta['status']}' in {filepath}")

    return meta


def collect_pages():
    pages = []
    titles = {}

    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue
            if file.startswith("_"):
                continue

            path = os.path.join(root, file)
            meta = parse_frontmatter(path)

            title = meta["title"]
            if title in titles:
                error(f"Duplicate title '{title}' in {path} and {titles[title]}")

            page = DocPage(path, meta)
            pages.append(page)
            titles[title] = path

    return pages, titles


def build_graph(pages, titles):
    children = defaultdict(list)
    roots = []

    for page in pages:
        if page.parent:
            if page.parent not in titles:
                error(f"Parent '{page.parent}' not found (referenced in {page.path})")
            children[page.parent].append(page)
        else:
            roots.append(page)

    for siblings in children.values():
        orders = {}
        for p in siblings:
            if p.nav_order in orders:
                error(
                    f"Duplicate nav_order {p.nav_order} under parent "
                    f"'{p.parent}' in {p.path} and {orders[p.nav_order]}"
                )
            orders[p.nav_order] = p.path

    return roots, children


def write_navigation_map(roots, children):
    def write_page(f, page, level=0):
        indent = "  " * level
        status = f" [{page.status}]" if page.status else ""
        f.write(f"{indent}- **{page.title}**{status}\n")

        for child in sorted(children.get(page.title, []), key=lambda x: x.nav_order):
            write_page(f, child, level + 1)

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("# Documentation Navigation Map\n\n")
        f.write("> Auto-generated. Do not edit manually.\n\n")

        for root in sorted(roots, key=lambda x: x.nav_order):
            write_page(f, root)


def main():
    print("🔍 Scanning documentation...")
    pages, titles = collect_pages()

    print("🔗 Building navigation graph...")
    roots, children = build_graph(pages, titles)

    print("🧭 Generating navigation map...")
    write_navigation_map(roots, children)

    print(f"✅ Navigation map generated at {OUTPUT_MD}")


if __name__ == "__main__":
    main()
