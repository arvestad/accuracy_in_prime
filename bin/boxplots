#! /usr/bin/env python2.7

import argparse
import sys
import re
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt


#sys.stderr.write("For some reason, boxplots.py wants to have env3.4 loaded. At least on Lasse's Mac")

def extract_lengths(filenames):
    lengths = []
    for f in filenames:
        matches = re.findall("\d+", f)
        assert len(matches) > 0, "No integers in filenames? " + str(filenames)
        lengths.append(int(max(matches)))
    return lengths

def main():
    parser = argparse.ArgumentParser(description="Combine several files with data into a single multi-box plot")
    parser.add_argument('-title', help="Plot title text, appears at top of plot")
    parser.add_argument('outputfilename', help="Where to put the PDF file")
    parser.add_argument('datafiles', nargs='+', help="Files with one value per line.")

    args = parser.parse_args()

    data = []
    lengths = extract_lengths(args.datafiles)

    try:
        for f in args.datafiles:
            dataset = []
            with open(f, 'r') as h:
                for line in h:
                    dataset.append(float(line))
            data.append(dataset)

    except Exception as e:
        sys.stderr.write("Error when trying to read data:\n")
        sys.stderr.write(str(e))
        return 1

    plt.figure()
    if args.title:
        plt.title(args.title)
    bp = plt.boxplot(data)
    plt.setp(bp['boxes'], color='black')
    plt.setp(bp['medians'], color='black')
    plt.setp(bp['fliers'], color='black')
    plt.setp(bp['whiskers'], color='black')
    plt.xticks(range(1,len(data)), lengths)
    plt.savefig(args.outputfilename)

    return 0

if __name__ == '__main__':
    sys.exit(main())
    
