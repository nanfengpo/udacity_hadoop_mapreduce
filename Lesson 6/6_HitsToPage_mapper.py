#!/usr/bin/python

import sys
import re

def mapper():
    for line in sys.stdin:
        data = re.sub('[][\"]', '', line).strip().split(" ")

        if len(data) == 10:
            ip, identity, username, date, timezone, method, address, protocol, code, byte = data
            if address == '/assets/js/the-associates.js':
                print "{0}\t{1}".format(address, 1)

def main():
    mapper()

if __name__ == '__main__':
  main()