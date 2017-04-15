#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, category, cost, payment = data
            print '{0}\t{1}'.format("Total Value of Sales: ", cost)

def main():
    mapper()

if __name__ == '__main__':
  main()