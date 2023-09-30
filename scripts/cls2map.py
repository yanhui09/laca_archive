#!/usr/bin/python
#-------------------
# Author: Yan Hui
# E-mail: huiyan@food.ku.dk
# Date: 29/12/2022

# group lines and the next if a string is found
import argparse
import os

def parse_arguments():
    """Read arguments from the console"""
    parser = argparse.ArgumentParser(description="Note: integrate LACA clusters into bin-read mapping file")
    parser.add_argument("-c", "--cluster", help='cluster directory')
    parser.add_argument("-o", "--output", help='bin-read mapping file as output')

    args = parser.parse_args()
    return args

# cluster directory: kmerCon/clusters/{cls}.csv
# {cls}.csv: seqid by line
# merged output.txt: {cls}_{suffix};nlines seqid
def cls2map(cls, output):
    # loop through .csv files under clusters directory
    with open(output, 'w') as out:
        for csv in os.listdir(cls):
            if csv.endswith('.csv'):
                with open(os.path.join(cls, csv), 'r') as f:
                    # read lines
                    lines = f.readlines()
                    suffix = ""
                    # csv;number of lines seqid pseduo-mm
                    c1 = csv.replace('.csv', suffix)+';'+str(len(lines))
                    for line in lines:
                        out.write(c1 + ' ' + line.strip() + ' 0\n')

def main():
    args = parse_arguments()
    if args.cluster:
        cls2map(args.cluster, args.output)
    else:
        print("Error: -c is required")
        exit()

if __name__ == "__main__":
    main()