#! /bin/bash

echo Testing mean_rf.sh:
echo -n "Computed: "
../mean_rf.py D1_true.newick D1_posterior.json
echo "Expected: 0.75*0 + 0.2 * 4 + 0.05 * 2 = 0.9"
echo



echo Testing bars.py:
../bars.py -title "My title" bar_chart < ./tree_sizes.tab && echo Output in bar_chart.pdf


