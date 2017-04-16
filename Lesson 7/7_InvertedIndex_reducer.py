#!/usr/bin/python

import sys

def reducer():
    wordCount = 0
    nodes = []
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisNode = data_mapped

        if oldKey and oldKey != thisKey:
            nodes.sort()
            if oldKey == "fantastic" or oldKey == "fantastically":
                print "{0}\t{1}\t{2}".format(oldKey, wordCount, nodes)
            wordCount = 0
            nodes = []

        oldKey = thisKey
        wordCount += 1
        nodes.append(int(thisNode))

    if oldKey != None and (oldKey == "fantastic" or oldKey == "fantastically"):
        print "{0}\t{1}".format(oldKey, wordCount, nodes)

def main():
    reducer()

if __name__ == '__main__':
    main()
