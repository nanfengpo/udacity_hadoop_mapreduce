#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        tagnames = line[2]
        nodetype = line[5]
        if nodetype == "question":
            print "{0}".format(tagnames)

def main():
    mapper()

if __name__ == '__main__':
    main()
