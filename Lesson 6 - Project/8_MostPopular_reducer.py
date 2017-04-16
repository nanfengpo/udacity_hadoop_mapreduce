#!/usr/bin/python

import sys

def reducer():
    currentCount = 0
    mostCountAddress = None
    mostCount = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey = data_mapped[0]

        if oldKey and oldKey != thisKey:
            currentCount = 0

        oldKey = thisKey
        currentCount += 1
        if currentCount > mostCount:
            mostCount = currentCount
            mostCountAddress = oldKey

    print "{0}\t{1}".format(mostCountAddress, mostCount)

def main():
    reducer()

if __name__ == '__main__':
    main()
