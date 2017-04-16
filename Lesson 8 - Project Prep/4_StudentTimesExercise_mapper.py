#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        author_id = line[3]
        added_at = line[8]

        if author_id == "author_id":
            continue

        print "{0}\t{1}".format(author_id, int(added_at[11:13]))

def main():
    mapper()

if __name__ == '__main__':
    main()
