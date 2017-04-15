#!/usr/bin/python

import sys

def reducer():
    count = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        oldKey = thisKey
        count += 1

    print "Number of hits from IP address {0}: {1}".format(oldKey, count)

def main():
    reducer()

if __name__ == '__main__':
    main()
