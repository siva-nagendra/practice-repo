#!C/Users/siva_/Anaconda3/ python
"""
Task
Read an integer N.
For all non-negative integers i<N , print i * i.
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

if __name__ == '__main__':
    n = int(input())
    if n >= 1:
        for eachNum in range(n):
            print (eachNum ** 2)
    else:
        pass