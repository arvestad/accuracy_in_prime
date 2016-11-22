#! /bin/bash

# This function will be called if there is kill signal to this script
_interupted() {
  echo "Caught SIGINT signal!" 
  kill -TERM "$child" 2>/dev/null
}

trap _interupted SIGINT

echo Starting test run
snakemake --config n_data_sets=10 seq_lengths="[25, 50]" n_iterations=100 thinning=10 &
child=$!

wait "$child"
