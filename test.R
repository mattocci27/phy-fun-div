library(tidyverse)

gl <- read_csv("data/gl_data.csv") |> janitor::clean_names()
pa <- read_csv("data/pa_data.csv") |> janitor::clean_names()

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
  geom_point() +
  facet_grid(
    trait ~ site,
    labeller = labeller(
      site = c(gl = "Global\n(interspecific)", pa = "Panama\n(intraspecific)"),
      trait = c(ll = "Leaf Lifespan", aarea = "Aarea" )
    ),
    switch = "y",
    scales = "free"
  ) +
  scale_x_log10() +
  scale_y_log10() +
  theme_minimal() +
  xlab("LMA") +
  ylab("") +
  theme(
    panel.border = element_rect(color = "black", fill = NA, linewidth = 0.5),
    strip.text.y.left = element_text(angle = 90, hjust = 0.5),
    strip.placement = "outside",
    legend.position = "none"
  )
