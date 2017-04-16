#!/usr/bin/python

import sys

def reducer():
    hoursCounter = [0] * 24
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisHour = data_mapped

        if oldKey and oldKey != thisKey:
            maxCount = max(hoursCounter)
            for index, item in enumerate(hoursCounter):
                if item == maxCount:
                    print '{0}\t{1}'.format(oldKey, index)
            hoursCounter = [0] * 24

        hoursCounter[int(thisHour)] += 1
        oldKey = thisKey

    if oldKey != None:
        maxCount = max(hoursCounter)
        for index, item in enumerate(hoursCounter):
            if item == maxCount:
                print '{0}\t{1}'.format(oldKey, index)

def main():
    reducer()

if __name__ == '__main__':
    main()
