#!/usr/bin/python

import sys

currentCount = 0
mostCountAddress = None
mostCount = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        currentCount = 0

    oldKey = thisKey
    currentCount += 1
    if currentCount > mostCount:
        mostCount = currentCount
        mostCountAddress = oldKey

print "{0}\t{1}".format(mostCountAddress, mostCount)
