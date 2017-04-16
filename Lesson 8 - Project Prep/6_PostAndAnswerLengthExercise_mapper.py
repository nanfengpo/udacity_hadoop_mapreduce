#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        if len(line) != 19:
            continue

        if not str(line[0]).isdigit():
            continue

        node_id = line[0]
        body = line[4]
        node_type = line[5]
        abs_parent_id = line[7]

        if node_type == "answer":
            node_id = abs_parent_id

        if node_type == "answer" or node_type == "question":
            print "{0}\t{1}\t{2}".format(node_id, node_type, len(body))

def main():
    mapper()

if __name__ == '__main__':
    main()
