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
