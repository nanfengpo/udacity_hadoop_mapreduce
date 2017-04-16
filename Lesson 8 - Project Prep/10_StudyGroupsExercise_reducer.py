#!/usr/bin/python

import sys

def reducer():
    users = []
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisAuthorID = data_mapped

        if oldKey and oldKey != thisKey:
            print '{0}\t{1}'.format(oldKey, users)
            users = []

        users.append(thisAuthorID)
        oldKey = thisKey

    if oldKey != None:
        print '{0}\t{1}'.format(oldKey, users)

def main():
    reducer()

if __name__ == '__main__':
    main()
