# Notes

## 2016-11-21

The figures in expereiments/length_variation*/figures/ did not look at
all what I had expected.  I realised that it was because I had
simulated with LGT! Same rate as duplications. Trying again. Running
both AA and DNA simulations. I should however probably consider to
simulate with higher duplication rate. The trees were a bit on the
small side in the first experiment. Actually, I should put together a
boxplot for tree sizes.

I also added a results directory. It will contain subdirectories named
after dates and will collect the figures (and more?) as they are
produced. Cannot really add traces though.

Should I consider compressing the traces?

Important: The same trees should be used for different sequence lengths!


## 2016-11-22

Bars charts now produced for tree sizes.

Changed data simulations so that the same trees are used no matter
what seq length is used. Hence, the same tree is the foundation for
sequence data of several lengths.

Added small script for removing old data: bin/cleanup.

Minimum tree size is now 10. I.e., on average 2 sequences per
species. So the data sets are still not very large. But it is a better
start, I guess.

Starting to use the configuration feature of snakemake for parameters
in common between experiments.

* `n_data_sets` -- decides how many gene families are created for each test.
* `seq_lengths` -- a list containing the lengths that we will try in
   the experiments of how length affects results.
