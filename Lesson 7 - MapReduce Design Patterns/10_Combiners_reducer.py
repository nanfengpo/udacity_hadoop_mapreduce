#!/usr/bin/python

import sys

def reducer():
    sales = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if oldKey and oldKey != thisKey:
            print '{0}\t{1}'.format(oldKey, sales)
            sales = float(thisSale)

        oldKey = thisKey
        sales += float(thisSale)

    if oldKey != None:
        print '{0}\t{1}'.format(oldKey, sales)

def main():
  reducer()

if __name__ == '__main__':
    main()
