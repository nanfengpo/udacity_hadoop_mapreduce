#!/usr/bin/python

import sys
import re

def mapper():
    for line in sys.stdin:
        data = re.sub('[][\"]', '', line).strip().split(" ")

        if len(data) == 10:
            ip, identity, username, date, timezone, method, address, protocol, code, byte = data
            print "{0}\t{1}".format(address.replace('http://www.the-associates.co.uk', ''), 1)

def main():
    mapper()

if __name__ == '__main__':
  main()