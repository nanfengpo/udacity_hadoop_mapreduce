#!/usr/bin/python

import sys

def reducer():
    salesTotal = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if oldKey and oldKey != thisKey:
            if oldKey == 'Toys' or oldKey == 'Consumer Electronics':
                print '{0}\t{1}'.format(oldKey, salesTotal)
            salesTotal = 0

        oldKey = thisKey
        salesTotal += float(thisSale)

    if oldKey != None and (oldKey == 'Toys' or oldKey == 'Consumer Electronics'):
        print '{0}\t{1}'.format(oldKey, salesTotal)

def main():
    reducer()

if __name__ == '__main__':
    main()