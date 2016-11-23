# Directories

* src/	Scripts and other source code. Working dir. When a script is ready (?), it is moved to the bin directory.
* bin/	Finished (?) scripts and programs. 
* java/	Location of JAR files, in particular for VMCMC. I am using am updated version, a prerelease of v1.1 sort-of, which "behaves better".
* species_trees/
	Location of species trees, duh. The whole range of trees we are interested in will be here.
* experiments/
	This is were the different test cases are worked on. 
* results/
	This is the destination of figures etc that are created when running experiments. Subdirectories are named with dates.
* old_effort
	Scripts etc that Annelie and Mehmood have put together. Mehmood's script can also be found in his github account.


# Files

Snakefile	The file that runs most of the project
bin/snake_testing
            Run a test-configuration of the experiemnts. Smaller dataset and fewer iterations.

# Dependencies

* Snakemake
* ETE2
* matplotlib



# Getting snakemake running on Ubuntu

First follow installation instructions for Snakemake. I created a Conda profile with:
```
conda create -n snakemake  -c bioconda  --file requirements.txt
```
where `requirements.txt` contained
```
python=3.5.1
snakemake=3.5.5
```

Then the profile is activated with:
```
source activate snakemake
```


