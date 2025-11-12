library(targets)
library(tarchetypes)
library(tidyverse)
library(furrr)
library(quarto)

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
    gl_data_csv,
    "data/gl_data.csv",
    format = "file"
  ),

  tar_target(
    pa_data_csv,
    "data/pa_data.csv",
    format = "file"
  ),

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

  tar_target(
    trait_plot_fig, {
      p <- trait_plot(gl_data_csv, pa_data_csv)
      my_ggsave(
        "images/trait_plot",
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
