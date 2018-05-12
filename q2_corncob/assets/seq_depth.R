#!/usr/bin/env Rscript

cat(R.version$version.string, "\n")
args <- commandArgs(TRUE)

out.path <- args[[1]]
freq.table_fp <- args[[2]]
freq.table <- read.csv(file = freq.table_fp)[,-1]
meta.data_fp <- args[[3]]
meta.data <- read.csv(file = meta.data_fp, sep = "\t")

# print(dim(freq.table))
# print(rowSums(freq.table))
# print(meta.data)

cat("Hey you loaded something! \n")


### LOAD LIBRARIES ###
#suppressWarnings(library(CORNCOB))
suppressWarnings(library(ggplot2))
#cat("CORNCOB R package version:", as.character(packageVersion("CORNCOB")), "\n")
seq_depth <- function(freq) {
  return(data.frame(rowSums(freq)))
}


plot_depth <- function(seqs) {
  df <- data.frame(depth = seqs,
                   index = 1:nrow(seqs))
  colnames(df)[1] <- "depth"
  ggplot2::ggplot(df, ggplot2::aes(x = index, y = depth)) +
    ggplot2::geom_point() +
    ggplot2::labs(x = "Sample", y = "Sequencing Depth", title = "Sequencing Depth") +
    ggplot2::theme_bw() +
    ggplot2::theme(plot.title = ggplot2::element_text(hjust = 0.5))
}

## write text warnings
fileConn <- file(paste0(out.path,"/warnings.txt"))
writeLines(c("Hello","World"), fileConn)
close(fileConn)

cat("You wrote warnings! \n")

## sink command: writes R output as a file
my_seq <- seq_depth(freq.table)
print(my_seq)
write.table(my_seq, file = paste0(out.path,"/mytable.tsv"), sep = "\t",
            row.names = TRUE, quote = FALSE)
cat("You wrote frequencies! \n")

plot_depth(my_seq)
ggplot2::ggsave(filename = paste0(out.path,"/plot.png"), width = 3, height = 3)

cat("You made a plot! \n")

# Have saved in out.path:
# warnings.txt
# mytable.tsv
# plot.png

q(status = 0)
