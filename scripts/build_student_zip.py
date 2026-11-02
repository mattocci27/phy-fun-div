#!/usr/bin/env python3
"""Package an explicit list of student files, optionally rendering the exercise.

Run from any directory: python3 scripts/build_student_zip.py
Requires only Python 3. --render also requires working Quarto/R packages.
"""

import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
FOLDER = "phy-fun-div"
FILES = (
    "diversity_example.qmd",
    "data/samp.csv",
    "data/dummy_trait.csv",
    "data/dummy_tree.newick",
    "appendixA.htm",
    "LICENSE",
    "assets/fontawesome-free-7.1.0-web/LICENSE.txt",
    "assets/fontawesome-free-7.1.0-web/css/all.min.css",
    "assets/fontawesome-free-7.1.0-web/js/all.min.js",
)
DIRECTORIES = (
    "assets/fontawesome-free-7.1.0-web/webfonts",
)
PROJECT = """Version: 1.0

RestoreWorkspace: No
SaveWorkspace: No
AlwaysSaveHistory: No

EnableCodeIndexing: Yes
UseSpacesForTab: Yes
NumSpacesForTab: 2
Encoding: UTF-8
"""
START = """AFEC 2026: Diversity calculation
================================

1. Extract the entire ZIP into a folder where you can save your work.
   Do not run files from inside the ZIP or move its files individually.
2. Have R and RStudio installed before class.
3. Double-click phy-fun-div.Rproj to open this folder as an RStudio project.
4. Open diversity_example.qmd in RStudio.
5. Run the install.packages(...) code under Prerequisites once, ideally
   before class. Package installation requires an internet connection.
6. Run the R chunks in order with their green play buttons. You do not
   need to render the document during class.

If diversity_example.html is included, open it in a browser to read the
worked example. Keep its accompanying folders beside it so that figures
and tables load. External links require internet access.

Git, cloning, and renv are not needed. The ZIP does not include R packages.

The relative-path demonstration deliberately tries a path that fails after
setwd("docs"). This is expected; continue with the following here::here()
chunks, including setwd(".."), to return to the project folder.

Contents:
- diversity_example.qmd: exercises and R code
- data/: the three datasets used in the exercises
- docs/: directory used in the relative-path demonstration
- appendixA.htm: reference table of diversity metrics
- assets/: fonts and scripts used by the notebook
- LICENSE: teaching-material license

Instructor: Masatoshi Katabuchi
Source: https://github.com/mattocci27/phy-fun-div
"""


def build(output: Path, render: bool = False) -> None:
    files = list(FILES)
    directories = list(DIRECTORIES)
    if render:
        # Refresh cached chunks so the handout matches the current source.
        subprocess.run(
            ["quarto", "render", "diversity_example.qmd", "--to", "html",
             "--cache-refresh"],
            cwd=ROOT, check=True,
        )
        files.append("diversity_example.html")
        directories.append("diversity_example_files")

    # Validate before creating/replacing the ZIP. No repository-wide globbing:
    # credentials, renv, slides, research data and caches stay out of the bundle.
    for name in files:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(ROOT / name)
    for name in directories:
        if not (ROOT / name).is_dir():
            raise FileNotFoundError(ROOT / name)

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="student-zip-") as temporary:
        stage = Path(temporary) / FOLDER
        stage.mkdir()
        for name in files:
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, target)
        for name in directories:
            shutil.copytree(
                ROOT / name, stage / name,
                ignore=shutil.ignore_patterns(".DS_Store", "*.map"),
            )
        (stage / "phy-fun-div.Rproj").write_text(PROJECT, encoding="utf-8")
        (stage / "START_HERE.txt").write_text(START, encoding="utf-8")
        (stage / "docs").mkdir()
        (stage / "docs" / "README.txt").write_text(
            "This directory is used by the here/relative-path exercise.\n",
            encoding="utf-8",
        )
        archive = Path(temporary) / "student.zip"
        with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(stage.parent))
        shutil.copyfile(archive, output)
    print(f"Created {output} ({output.stat().st_size / 1024 / 1024:.2f} MB)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=ROOT / "dist" / "phy-fun-div-student.zip",
        help="ZIP destination (default: dist/phy-fun-div-student.zip)",
    )
    parser.add_argument(
        "--render", action="store_true",
        help="Render and include current HTML results (requires Quarto and R packages)",
    )
    args = parser.parse_args()
    build(args.output.resolve(), render=args.render)


if __name__ == "__main__":
    main()
