#!/usr/bin/python

import sys
import re

def mapper():
    oldNode = None
    for line in sys.stdin:
        data = re.findall(r"[\w]+", line.lower())
        if data:
            currentNode = data[0]
            if currentNode.isdigit():
                for word in data[1:]:
                    print "{0}\t{1}".format(word, currentNode)
                oldNode = currentNode
            elif oldNode:
                for word in data[1:]:
                    print "{0}\t{1}".format(word, oldNode)

def main():
    mapper()

if __name__ == '__main__':
  main()