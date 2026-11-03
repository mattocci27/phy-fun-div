#!/usr/bin/env python3
"""Stage the rendered teaching materials for GitHub Pages (no R needed).

Render changed .qmd files locally and commit their HTML/assets before publishing.
Only the files listed here are copied; logs and the R environment stay local.
"""

from html.parser import HTMLParser
from pathlib import Path
import shutil
import tempfile
from urllib.parse import unquote, urlsplit

from build_student_zip import build as build_student_zip

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "pages"
FILES = ("index.html", "main.html", "diversity_example.html", "appendixA.htm", "LICENSE")
DIRECTORIES = ("assets", "images", "figure", "libs", "main_files", "diversity_example_files")


class LocalReferences(HTMLParser):
    """Collect local resources, including Reveal.js lazy-loaded images."""

    def __init__(self) -> None:
        super().__init__()
        self.paths: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key not in ("src", "href", "data-src", "data-background-image") or not value:
                continue
            url = urlsplit(value)
            if not url.scheme and not url.netloc and url.path:
                self.paths.add(unquote(url.path))


def validate_site(site: Path) -> None:
    """Fail the build rather than publish HTML with missing local resources."""
    missing = []
    for name in ("index.html", "main.html", "diversity_example.html"):
        parser = LocalReferences()
        parser.feed((site / name).read_text(encoding="utf-8"))
        for reference in sorted(parser.paths):
            target = site / reference.lstrip("/")
            if not target.exists():
                missing.append(f"{name}: {reference}")
    if missing:
        raise FileNotFoundError("Missing public resources:\n" + "\n".join(missing))


def main() -> None:
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    for name in DIRECTORIES:
        if not (ROOT / name).is_dir():
            raise FileNotFoundError(ROOT / name)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pages-", dir=OUTPUT.parent) as temporary:
        stage = Path(temporary) / "site"
        stage.mkdir()
        for name in FILES:
            shutil.copy2(ROOT / name, stage / name)
        for name in DIRECTORIES:
            shutil.copytree(
                ROOT / name, stage / name,
                ignore=shutil.ignore_patterns(".DS_Store", "*.map"),
            )
        build_student_zip(stage / "phy-fun-div-student.zip")
        (stage / ".nojekyll").touch()
        validate_site(stage)
        if OUTPUT.exists():
            shutil.rmtree(OUTPUT)
        shutil.move(str(stage), OUTPUT)
    print(f"Pages files ready: {OUTPUT}")


if __name__ == "__main__":
    main()
