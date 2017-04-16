#!/usr/bin/python

import sys
import operator

def reducer():
    tags = []

    for line in sys.stdin:
        data_mapped = line.strip().split(" ")

        for item in data_mapped:
            if len(item) > 0:
                tags.append(item)

    tags.sort()
    counts = [[0 for i in range(2)] for j in range(len(tags))]
    idx = 0
    for index, item in enumerate(tags):
        if item != counts[idx][1]:
            idx += 1
        counts[idx][0] += 1
        counts[idx][1] = item

    counts.sort(reverse=True)
    for i in range (0, 10):
        print "{0}\t{1}".format(counts[i][1], counts[i][0])

def main():
    reducer()

if __name__ == '__main__':
    main()
