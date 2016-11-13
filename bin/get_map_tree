#! /usr/bin/env python2.7

import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Read a JSON file created by VMCMC, to read the MAP tree")
    parser.add_argument('mapfile', help="JSON file, created by 'VMCMC -m', containing a MAP tree.")

    args = parser.parse_args()

    try:
        with open(args.mapfile, 'r') as ih:
            data = json.load(ih)
    except Exception as e:
        sys.stderr.write("Error when trying to get the MAP tree:\n")
        sys.stderr.write(str(e))
        return 1

    try:
        t = data['Series'][0]['MAP_Tree']
        sys.stdout.write(t + "\n")
        return 0
    except Exception as e:
        sys.stderr.write('Error when trying to access MAP tree in the JSON file:\n')
        sys.stderr.write(str(e))
        return 2

if __name__ == '__main__':
    sys.exit(main())
    
