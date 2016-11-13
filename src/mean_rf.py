#! /usr/bin/env python2.7

import ete2
import json
import argparse
import sys

def mean_rf(t, posterior):
    '''
    t is an ETE tree and posterior is a list representing the posterior, generated by VMCMC.
    '''
    rf_sum = 0
    for elem in posterior:
        t_i = ete2.Tree(elem['Newick'])
        p_i = elem['Posterior probability']
        res = t.compare(t_i)
        rf = res['rf']
        rf_sum += p_i * rf

    return rf_sum


def main():
    parser = argparse.ArgumentParser(description="Compute mean Robinson-Foulds distance  between a tree and a tree posterior, as estimated by JPrIME/VMCMC.")
    parser.add_argument('t', help="File with tree on Newick format")
    parser.add_argument('posterior', help="File with posterior on VMCMC's JSON format")

    args = parser.parse_args()

    try:
        with open(args.t, 'r') as h1, open(args.posterior, 'r') as h2:
            t = ete2.Tree(h1.read())
            raw_posterior = json.load(h2)
            posterior = raw_posterior['Trees']['Series_0'] # The naming scheme here is unfortunate. Very arbitrary.
    except IOError as e:
        sys.stderr.write("Error when trying to read file:\n")
        sys.stderr.write(str(e))
        return 1
    except Exception as e:
        sys.stderr.write("Error when loading data:\n")
        sys.stderr.write(str(e))
        return 2

    
    res = mean_rf(t, posterior)
    print res
    return 0

if __name__ == '__main__':
    sys.exit(main())
    
