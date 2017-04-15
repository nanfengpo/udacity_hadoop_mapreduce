#!/usr/bin/python

import sys
import re

def mapper():
    for line in sys.stdin:
        data = re.sub('[][\"]', '', line).strip().split(" ")

        if len(data) == 10:
            ip, identity, username, date, timezone, method, address, protocol, code, byte = data
            if ip == '10.99.99.186':
                print "{0}\t{1}".format(ip, 1)

def main():
    mapper()

if __name__ == '__main__':
  main()