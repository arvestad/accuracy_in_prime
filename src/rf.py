#! /usr/bin/env python2.7

import ete2
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Compute Robinson-Foulds distance between two trees")
    parser.add_argument('t1', help="File with tree on Newick format")
    parser.add_argument('t2', help="File with tree on Newick format")

    args = parser.parse_args()

    try:
        with open(args.t1, 'r') as h1, open(args.t2, 'r') as h2:
            t1 = ete2.Tree(h1.read())
            t2 = ete2.Tree(h2.read())
    except Exception as e:
        sys.stderr.write("Error when trying to read tree file:\n")
        sys.stderr.write(str(e))
        return 1

    res = t1.compare(t2)
    print res['rf']
    return 0

if __name__ == '__main__':
    sys.exit(main())
    
