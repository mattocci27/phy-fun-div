install.packages("magick")
library(magick)

img <- image_read("images/LES2004.png")
info <- image_info(img)

w <- info$width
h <- floor(info$height / 4)

# Divide the original image into four panels
panels <- lapply(0:3, function(i) {
  image_crop(img, paste0(w, "x", h, "+0+", i * h))
})

# Rearrange into a 2 × 2 layout
top <- image_append(c(panels[[1]], panels[[2]]))
bottom <- image_append(c(panels[[3]], panels[[4]]))

combined <- image_append(c(top, bottom), stack = TRUE)

image_write(combined, "images/LES2004_2x2.png")
