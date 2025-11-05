Sys.setenv(RENV_DOWNLOAD_METHOD = "curl")
Sys.setenv(RENV_CONFIG_PAK_ENABLED = "TRUE")
options(renv.install.staged = FALSE)

if (file.exists("renv/activate.R")) {
  source("renv/activate.R")
  if ("renv" %in% loadedNamespaces()) {
    renv::settings$use.cache(TRUE)
  }
}
