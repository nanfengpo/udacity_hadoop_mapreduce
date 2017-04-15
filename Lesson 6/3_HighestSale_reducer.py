#!/usr/bin/python

import sys

def reducer():
    highestSale = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if oldKey and oldKey != thisKey:
            if oldKey == 'Reno' or oldKey == 'Toledo' or oldKey == 'Chandler':
                print '{0}\t{1}'.format(oldKey, highestSale)
            highestSale = float(thisSale)

        oldKey = thisKey
        highestSale = max(float(thisSale), highestSale)

    if oldKey != None and (oldKey == 'Reno' or oldKey == 'Toledo' or oldKey == 'Chandler'):
        print '{0}\t{1}'.format(oldKey, highestSale)

def main():
        reducer()

if __name__ == '__main__':
  main()
