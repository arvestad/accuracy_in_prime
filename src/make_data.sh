#! /bin/bash

cd sim_data

PROJDIR=/Users/arve/projects/accuracy_in_prime
SIMULATE=$PROJDIR/src/simulationGFI.py
S=$PROJDIR/species_trees/real.newick
JPRIME=/Users/arve/opt/jprime-latest/jprime-0.3.4.jar

# -n <i>  -> generate <i> trees
N=2

# -O <outputdir>

#-m <minper>  -> generate at least <minper> genes per species leaf in $S
MINPER=1

# Test case 1a: DNA of varying lengths
cd testcase1_dna
for L in 50 100; do # 200 300 400 500 750 1000; do
    dirname=L_$L
    $SIMULATE -stree $S -j $JPRIME -n $N -O $dirname -m $MINPER -L $L -M HKY
done
cd ..

# Test case 1b: AA of varying lengths


# Done!
cd ..
