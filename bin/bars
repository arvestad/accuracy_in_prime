#! /usr/bin/env python2.7

import argparse
import sys
import re
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt



def main():
    parser = argparse.ArgumentParser(description="Use output from 'uniq -c' in a bar plot. Read from stdin.")
    parser.add_argument('-title', help="Plot title text, appears at top of plot")
    parser.add_argument('outputfilename', help="Where to put the PDF file")

    args = parser.parse_args()

    heights = []
    sorted_items = []
    try:
        for line in sys.stdin:
            count, item = line.split()
            heights.append(int(count))
            sorted_items.append(int(item))

    except Exception as e:
        sys.stderr.write("Error when trying to read data:\n")
        sys.stderr.write(str(e))
        return 1

    plt.figure()
    if args.title:
        plt.title(args.title)
    bp = plt.bar(sorted_items, heights, color='gray')
    plt.savefig(args.outputfilename)

    return 0

if __name__ == '__main__':
    sys.exit(main())
    
