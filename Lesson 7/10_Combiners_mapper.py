#!/usr/bin/python

import sys
from datetime import datetime

def mapper():
    cost = [0] * 7
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 7:
            date, time, store, category, cost, payment = data
            weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
            cost[int(weekday)] += cost

    for i in range(0, 7):
        print "{0}\t{1}".format(i, cost[i])

def main():
    mapper()

if __name__ == '__main__':
  main()