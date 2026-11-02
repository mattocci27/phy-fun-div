#!/usr/bin/env python3
"""Stage the rendered teaching materials for GitHub Pages (no R needed).

Render changed .qmd files locally and commit their HTML/assets before publishing.
Only the files listed here are copied; logs and the R environment stay local.
"""

from pathlib import Path
import shutil
import tempfile

from build_student_zip import build as build_student_zip

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "pages"
FILES = ("index.html", "main.html", "diversity_example.html", "appendixA.htm", "LICENSE")
DIRECTORIES = ("assets", "images", "libs", "main_files", "diversity_example_files")


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
        if OUTPUT.exists():
            shutil.rmtree(OUTPUT)
        shutil.move(str(stage), OUTPUT)
    print(f"Pages files ready: {OUTPUT}")


if __name__ == "__main__":
    main()
