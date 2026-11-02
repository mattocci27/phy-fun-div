[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# AFEC 2026: Phylogenetic diversity, functional diversity and trait-based approaches

Lecture slides and R exercises for the AFEC 2026 workshop at XTBG, CAS, November 3–4, 2026. Instructor: Masatoshi Katabuchi.

- Slides: <https://mattocci27.github.io/phy-fun-div/main.html>
- Hands-on notebook: <https://mattocci27.github.io/phy-fun-div/diversity_example.html>
- Student ZIP: <https://mattocci27.github.io/phy-fun-div/phy-fun-div-student.zip>

## Student Quick Start

1. Install R and RStudio before class.
2. Download `phy-fun-div-student.zip` provided by the instructor and extract the entire folder. Do not open files inside the ZIP.
3. Open `phy-fun-div.Rproj` in RStudio, then open `diversity_example.qmd`.
4. Install the required packages once by running this code in the R console (internet required; please do this before class):

    ```r
    install.packages(c(
      "tidyverse", "picante", "FD",
      "DT", "here", "vegan", "ape"
    ))
    ```

5. Run the R code chunks in order using their green play buttons. Keep the datasets and accompanying folders in place.

Git and `renv` are not needed for the student ZIP. Rendering the notebook is optional; during class, run individual chunks. If `diversity_example.html` is included, open it in a browser to read the worked example.

The exercises cover species richness and Shannon diversity, phylogenetic PD/MPD/MNTD, community-weighted means, functional distances, and comparison with null models.

## Instructor Setup

For editing and rendering the full teaching materials, clone this repository and open `phy-fun-div.Rproj`. The repository uses `renv` for its development environment:

```r
renv::restore()
```

With Quarto and the required R packages installed, render the materials using:

```bash
quarto render main.qmd
quarto render diversity_example.qmd
```

## Directory Layout

```
.
|-- main.qmd               # Primary Quarto presentation
|-- diversity_example.qmd  # Hands-on tutorial notebook (students run this file)
|-- assets/                # CSS themes and custom styling
|-- data/                  # Community, trait, tree, and leaf-trait datasets
|-- scripts/build_student_zip.py  # Generate the student handout ZIP
|-- dist/                  # Generated student ZIP (not tracked by Git)
|-- phy-fun-div.Rproj      # RStudio project
|-- docs/                  # Teaching notes; also used for the path demonstration
|-- images/                # Figures used throughout the slides
|-- figure/                # Auto-generated plot outputs
|-- R/                     # Helper functions and package setup
|-- run.R                  # Run the targets pipeline
|-- renv/                  # renv metadata (auto-managed)
|-- renv.lock              # Locked package versions
|-- main_files/            # Assets generated for the slide deck
`-- _targets*/             # Targets pipeline and retained metadata
```

## Development Notes

- Maintainers manage dependencies with `renv` (using `pak` for faster installs), but students can rely on the base `install.packages()` call above.
- Use the explicit `quarto render` commands above to rebuild the teaching materials.
- The project follows the CC BY-SA 4.0 license—re-use is welcome with attribution.
- Font Awesome Free 7.1.0 runtime assets (CSS, JS, and webfonts) are included locally under `assets/fontawesome-free-7.1.0-web/` with their license.
- `Rscript run.R` runs the targets pipeline, including figure generation from `data/gl_data.csv` and `data/pa_data.csv`. The `_targets/meta` metadata is retained intentionally.
- `scripts/prepare_les_figure.R` prepares the LES panel figure; run it from the project root with the `magick` package installed.
- Multiplex synchronization is disabled for public slides. Do not distribute a speaker HTML containing synchronization credentials.

## Participant Files

Build the student handout with Python 3 (no extra Python packages needed):

```bash
python3 scripts/build_student_zip.py
```

This writes `dist/phy-fun-div-student.zip`. Distribute this ZIP to students. They extract
the whole folder, read `START_HERE.txt`, open `phy-fun-div.Rproj` in RStudio,
install the listed R packages, and run chunks in `diversity_example.qmd`.
Git and `renv` are not required.

The bundle includes only the exercise, its three input datasets, display
dependencies, the reference appendix, licenses, and a small RStudio project.
The `docs/` directory supports the relative-path demonstration. Slides,
research files, caches, and the instructor's R environment are excluded.

To include a freshly rendered HTML handout and its figures, run
`python3 scripts/build_student_zip.py --render` with the instructor's working
R/Quarto environment. This refreshes notebook caches before packaging; if rendering
fails, the ZIP is not replaced. Use `--output /path/to/handout.zip` to choose
another destination.

## References

- Swenson, N. G. (2013). *Ecography* 36, 264–276.
- Swenson, N. G. (2012). Phylogenetics & Traits Workshop, National Dong Hwa University.
- Vellend, M. (2016). *The Theory of Ecological Communities*. Princeton University Press.
- [DanyangDai/brownbag_2022_10_11](https://github.com/DanyangDai/brownbag_2022_10_11)
- [emitanaka/talks](https://github.com/emitanaka/talks)

## GitHub Pages

The `Publish teaching materials` workflow publishes on pushes to `main`, or can
be run manually from Actions. In repository **Settings → Pages → Build and
deployment**, select **GitHub Actions** as the source.

Before pushing a changed `.qmd`, render it locally and include its generated
HTML and assets in the commit. The workflow publishes these reviewed outputs;
it does not install R packages or rerun the analyses on GitHub.

```bash
quarto render main.qmd
quarto render diversity_example.qmd
python3 scripts/build_pages.py
```

`dist/pages/` is the complete public site. The root URL opens the slides;
the exercise and student ZIP have the direct links above. The staging script
copies an explicit set of presentation files, generates the student ZIP, and
excludes `logs/`, raw research datasets, caches, and `renv/` from the website.
This does not remove files from the repository's Git history.
