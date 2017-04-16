#!/usr/bin/python

import sys

def reducer():
    sales = 0
    weekdayCount = 0
    weekday = 6

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisSale = data_mapped

        if int(thisKey) == weekday:
            sales += float(thisSale)
            weekdayCount += 1

    mean = sales / weekdayCount
    print "Mean value of sales on Sunday: {0}".format(mean)

def main():
        reducer()

if __name__ == '__main__':
  main()
