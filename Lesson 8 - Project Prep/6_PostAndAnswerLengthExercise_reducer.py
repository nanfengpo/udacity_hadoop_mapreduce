#!/usr/bin/python

import sys

def reducer():
    answerLength = 0
    answerCount = 0
    questionLength = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 3:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisNodeType, thisBodyLength = data_mapped

        if oldKey and oldKey != thisKey:
            print '{0}\t{1}\t{2}'.format(oldKey, questionLength, float(answerLength) / float((answerCount if answerCount > 0 else 1)))
            answerCount = 0
            answerLength = 0
            questionLength = 0

        if thisNodeType == "answer":
            answerLength += int(thisBodyLength)
            answerCount += 1
        elif thisNodeType == "question":
            questionLength = int(thisBodyLength)
        oldKey = thisKey

    if oldKey != None:
        print '{0}\t{1}\t{2}'.format(oldKey, questionLength, float(answerLength) / float((answerCount if answerCount > 0 else 1)))

def main():
    reducer()

if __name__ == '__main__':
    main()
