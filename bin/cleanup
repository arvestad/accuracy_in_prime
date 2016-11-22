#! /bin/bash

cd experiments
for i in `ls -d */`; do
    echo $i
    pushd $i && rm -rf traces assessment sim_data figures && popd
done
