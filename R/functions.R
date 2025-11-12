#' @title ggsave for targets
my_ggsave <- function(filename, plot, units = c("in", "cm",
        "mm", "px"), height = NA, width = NA, dpi = 300, ...) {
  ggsave(
    filename = paste0(filename, ".png"),
    plot = plot,
    height = height,
    width = width,
    units = units,
    dpi = dpi,
    ...
  )
  ggsave(
    filename = paste0(filename, ".pdf"),
    plot = plot,
    height = height,
    width = width,
    units = units,
    dpi = dpi,
    ...
  )
  str_c(filename, c(".png", ".pdf"))
}

plot_ex_tree <- function(size = 0.8) {
  data(chiroptera, package="ape")
  groupInfo <- split(chiroptera$tip.label, gsub("_\\w+", "", chiroptera$tip.label))
  chiroptera <- ggtree::groupOTU(chiroptera, groupInfo)
  attr(chiroptera, "subgroup") <- attr(chiroptera, "group")

  ggtree::ggtree(chiroptera, mapping = ggplot2::aes(color = group), layout = "circular") +
    ggtree::geom_tiplab(mapping = ggplot2::aes(angle = angle), size = size) +
    ggplot2::theme(legend.position = "none")
}


trait_plot <- function(csv_gl, csv_pa) {

  gl <- read_csv(csv_gl) |> janitor::clean_names()
  pa <- read_csv(csv_pa) |> janitor::clean_names()

  gl2 <- gl |>
    dplyr::select(sp, lma, ll, aarea) |>
    mutate(site = "gl")
  pa2 <- pa |>
    dplyr::select(sp, lma, ll, aarea) |>
    mutate(site = "pa")

  df <- bind_rows(gl2, pa2) |>
    pivot_longer(cols = c(ll, aarea), names_to = "trait", values_to = "value") |>
    mutate(
      trait = factor(trait, levels = c("ll", "aarea")),
      site = factor(site, levels = c("gl", "pa"))
    )

  p <- ggplot(df, aes(x = lma, y = value, color = site)) +
    geom_point(alpha = 0.8) +
    facet_grid(
      trait ~ site,
      labeller = labeller(
        site = c(gl = "Global\n(interspecific)", pa = "Panama\n(intraspecific)"),
        trait = c(
          ll = "Leaf lifespan (months)",
          aarea = "Aₐᵣₑₐ (µmol m⁻² s⁻¹)"
        )
      ),
      switch = "y",
      scales = "free"
    ) +
    scale_color_manual(values = c(gl = "#0072B2", pa = "#D55E00")) +
    scale_x_log10() +
    scale_y_log10() +
    theme_minimal() +
    xlab("LMA (g m⁻²)") +
    ylab("") +
    theme(
      panel.border = element_rect(color = "black", fill = NA, linewidth = 0.5),
      strip.text = element_text(face = "bold", size = 12),
      strip.text.y.left = element_text(angle = 90, hjust = 0.5, size = 12, face = "bold"),
      axis.title.x = element_text(size = 12, face = "bold"),
      strip.placement = "outside",
      legend.position = "none"
    )
  p
}
