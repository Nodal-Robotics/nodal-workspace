import yaml
from pathlib import Path
from collections import defaultdict

DOCS_DIR = Path("docs")

class DocError(Exception):
    pass

class Page:
    def __init__(self, title, parent, nav_order, path):
        self.title = title
        self.parent = parent
        self.nav_order = nav_order
        self.path = path
        self.is_index = path.name == "index.md"

def load_pages():
    pages = {}
    for md in DOCS_DIR.rglob("*.md"):
        with md.open() as f:
            content = f.read()

        if not content.startswith("---"):
            raise DocError(f"Missing frontmatter in {md}")

        fm_text = content.split("---", 2)[1]
        fm = yaml.safe_load(fm_text)

        title = fm.get("title")
        nav_order = fm.get("nav_order")
        parent = fm.get("parent")

        if not title or nav_order is None:
            raise DocError(f"Missing title or nav_order in {md}")

        if title in pages:
            raise DocError(f"Duplicate title '{title}' in {md} and {pages[title].path}")

        pages[title] = Page(title, parent, nav_order, md)

    return pages

def validate_parents(pages):
    for page in pages.values():
        if page.parent:
            if page.parent not in pages:
                raise DocError(f"Parent '{page.parent}' not found for {page.path}")
            if page.parent == page.title:
                raise DocError(f"Page cannot be its own parent: {page.title}")

def detect_cycles(pages):
    def visit(title, stack):
        if title in stack:
            raise DocError(f"Cycle detected: {' -> '.join(stack + [title])}")
        page = pages[title]
        if page.parent:
            visit(page.parent, stack + [title])

    for title in pages:
        visit(title, [])

def validate_nav_order(pages):
    children = defaultdict(list)
    for page in pages.values():
        parent = page.parent or "__ROOT__"
        children[parent].append(page)

    for parent, group in children.items():
        seen = {}
        for page in group:
            if page.nav_order in seen:
                other = seen[page.nav_order]
                raise DocError(
                    f"nav_order conflict under parent '{parent}': "
                    f"{page.path} and {other.path}"
                )
            seen[page.nav_order] = page

def main():
    pages = load_pages()
    validate_parents(pages)
    detect_cycles(pages)
    validate_nav_order(pages)

    print("✔ Documentation navigation graph is valid")

if __name__ == "__main__":
    main()
