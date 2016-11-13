# Directories

src/	Scripts and other source code. Working dir. When a script is ready (?), it is moved to the bin directory.
bin/	Finished (?) scripts and programs. 
java/	Location of JAR files, in particular for VMCMC. I am using am updated version, a prerelease of v1.1 sort-of, which "behaves better".
species_trees/
	Location of species trees, duh. The whole range of trees we are interested in will be here.
experiments/
	This is were the different test cases are worked on. 
figures/
	This is the destination of figures that are created from the results.
AnnelieEffort/
	Scripts etc that Annelie put together
MehmoodSimulationScript/
	The script Mehmood has used to generate data. It is from his github account, but I am tweaking it to my desire.

# Files

Snakefile	The file that runs most of the project
make_data.sh	Found in src, runs Mehmood's simulation script

# Dependencies

* ETE2
* matplotlib
