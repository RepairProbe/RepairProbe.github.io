#!/usr/bin/env python3
"""Check public static pages with Python's standard library; no network required."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.references = []
        self.robots = set()
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value is not None:
                self.references.append((value, self.getpos()[0]))
        if tag == "meta" and attrs.get("name", "").lower() == "robots":
            self.robots.update(re.split(r"[\s,]+", attrs.get("content", "").lower()))

    handle_startendtag = handle_starttag


def check_site(root):
    """Return actionable errors for top-level public pages and their local targets."""
    root = root.resolve()
    pages = {path: Page(path) for path in sorted(root.glob("*.html"))}
    errors = []
    if not pages:
        return ["No public HTML pages found"]
    not_found = root / "404.html"
    if not_found not in pages:
        errors.append("404.html: missing error page")
    elif "noindex" not in pages[not_found].robots:
        errors.append("404.html: robots metadata must include noindex")

    for source, page in pages.items():
        label = source.relative_to(root)
        for element_id, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f"{label}: duplicate id {element_id!r}")
        for reference, line in page.references:
            location = f"{label}:{line}"
            parts = urlsplit(reference)
            # Mail links and links to other origins are outside this offline check.
            if parts.scheme not in ("", "http", "https"):
                continue
            if parts.netloc and parts.hostname != "repairprobe.github.io":
                continue
            if source == not_found and parts.path and not (
                parts.path.startswith("/") or parts.netloc
            ):
                errors.append(f"{location}: 404 path must be root-relative: {reference}")
            decoded = unquote(parts.path)
            if not decoded:
                target = source
            elif decoded.startswith("/"):
                target = root / decoded.lstrip("/")
            else:
                target = source.parent / decoded
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{location}: path escapes site root: {reference}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"{location}: missing local target: {reference}")
                continue
            if parts.fragment and target.suffix.lower() == ".html":
                if target not in pages:
                    pages_target = Page(target)
                else:
                    pages_target = pages[target]
                if unquote(parts.fragment) not in pages_target.ids:
                    errors.append(f"{location}: missing anchor: {reference}")
    return errors


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = check_site(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Site check passed: internal links/anchors, unique IDs, 404 paths and noindex")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
