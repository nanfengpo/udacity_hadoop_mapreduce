#!/usr/bin/python

import sys

def reducer():
    salesTotal = 0
    count = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        oldKey = thisKey
        salesTotal += float(thisSale)
        count += 1

    print '{0}\t{1}'.format(oldKey, salesTotal)
    print "Number of Sales: {0}".format(count)

def main():
    reducer()

if __name__ == '__main__':
    main()
