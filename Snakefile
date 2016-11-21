JPRIME="java -jar ../../java/jprime.jar"
VMCMC="java -jar ../../java/vmcmc.jar"
GETMAPTREE="../../bin/get_map_tree"
BOXPLOTS="../../bin/boxplots"
S = "../../species_trees/H1.newick"
ITERATIONS="1000000"
THINNING="100"

subworkflow download_software:
   snakefile: "download_software.snake"

subworkflow length_variation_dna:
   workdir: "experiments/length_variation_dna/"
   snakefile: "experiments/length_variation_dna/Snakefile"

subworkflow length_variation_aa:
   workdir: "experiments/length_variation_aa/"
   snakefile: "experiments/length_variation_aa/Snakefile"

rule all:
   input:
      download_software("java/jprime.jar"),
      download_software("java/vmcmc.jar"),
      length_variation_dna("figures/rf_summary.pdf"),
      length_variation_dna("figures/rfm_summary.pdf"),
      length_variation_aa("figures/rf_summary.pdf"),
      length_variation_aa("figures/rfm_summary.pdf")
