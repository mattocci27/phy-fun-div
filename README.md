[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# AFEC2025: Phylogenetic diversity, functional diversity and trait-based approaches

Quarto slide deck and supporting material for the AFEC 2025 workshop on phylogenetic diversity, functional diversity, and trait-based approaches hosted at XTBG.

- Slides: <https://forest-canopy.github.io/assets/phy-fun-div/main.html>
- Hands-on notebook: <https://forest-canopy.github.io/assets/phy-fun-div/diversity_example.html>

## Quick Start

1. Install R (≥ 4.3) and Quarto (≥ 1.4).
2. Clone this repository and open it in R (e.g., via RStudio or radian).
3. Optional: Restore the exact development environment with `renv`.

   ```r
   renv::restore()
   ```

   > Tip: If you prefer to skip `renv`, start R with `RENV_CONFIG_AUTOLOADER_ENABLED=FALSE` (for example, run `Sys.setenv(RENV_CONFIG_AUTOLOADER_ENABLED = "FALSE")` before loading packages) or temporarily comment out the lines in `.Rprofile` that source `renv/activate.R`.

4. Install the R packages used in `diversity_example.qmd` (you can copy/paste the following into the R console):

    ```r
   install.packages(c(
     "tidyverse", "fontawesome", "picante",
     "FD", "DT", "here", "vegan", "ape"
   ))
    ```

5. Open `diversity_example.qmd` and work through the exercises (students only need this document plus the datasets in `data/`).

6. Optional: Render the main slide deck:

   ```bash
   quarto render main.qmd
   ```

7. Optional: regenerate the diversity example notebook.

   ```bash
   quarto render diversity_example.qmd
   ```

## Directory Layout

```
.
|-- main.qmd               # Primary Quarto presentation
|-- diversity_example.qmd  # Hands-on tutorial notebook (students run this file)
|-- assets/                # CSS themes and custom styling
|-- data/                  # Example trait, tree, and soil datasets (used by students)
|-- images/                # Figures used throughout the slides
|-- figure/                # Auto-generated plot outputs
|-- R/                     # Helper functions and package setup
|-- run.R / run.sh         # Convenience scripts for rendering
|-- renv/                  # renv metadata (auto-managed)
|-- renv.lock              # Locked package versions
|-- README_files/          # Assets generated for the README
|-- main_files/            # Assets generated for the slide deck
`-- _targets*/             # Targets pipeline artefacts
```

## Development Notes

- Maintainers manage dependencies with `renv` (using `pak` for faster installs), but students can rely on the base `install.packages()` call above.
- Rendering scripts (`run.R`, `run.sh`) wrap common build tasks; feel free to adapt them for batch workflows.
- The project follows the CC BY-SA 4.0 license—re-use is welcome with attribution.
- Font Awesome icons load via the CDN version 7.1.0; if you need offline assets, download the latest “Font Awesome Free” archive from <https://fontawesome.com/download> and adjust the paths accordingly.

## Participant Files

- Students only need to open `diversity_example.qmd` and use the datasets stored in `data/`.
- All other files support slide rendering, instructor workflows, or cached outputs.

## References

- Swenson, N. G. (2013). *Ecography* 36, 264–276.
- Swenson, N. G. (2012). Phylogenetics & Traits Workshop, National Dong Hwa University.
- Vellend, M. (2016). *The Theory of Ecological Communities*. Princeton University Press.
- [DanyangDai/brownbag_2022_10_11](https://github.com/DanyangDai/brownbag_2022_10_11)
- [emitanaka/talks](https://github.com/emitanaka/talks)
