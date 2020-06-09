#!C/Users/siva_/Anaconda3/ python
"""
Task
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

if __name__ == '__main__':
    n = int(input())
    for eachNum in (range(1, (n + 1))):
        print (eachNum, end = "")