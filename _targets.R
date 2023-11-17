library(targets)
library(tarchetypes)
library(tidyverse)
library(furrr)

# plan(multicore)
# options(clustermq.scheduler = "multicore")

source("R/functions.R")

tar_option_set(packages = c(
  "tidyverse",
  "patchwork",
  "here",
  "ape",
  "ggtree"
))

list(
  tar_target(
    ex_tree, {
      p <- plot_ex_tree(size = 0.8)
      my_ggsave(
        "images/tree_bg",
       p,
       dpi = 300,
       height = 12,
       width = 12,
       units = "cm"
      )
    },
    deployment = "main",
    format = "file"
  ),

  tar_quarto(
    main,
    "main.qmd"
    ),
  tar_quarto(
    div_ex,
    "diversity_example.qmd"
    ),
  NULL
)

