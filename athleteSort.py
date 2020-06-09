#!/Anaconda3/ python
"""
Task
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
You are required to sort the data based on the the K attribute and print the final resulting table
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

from operator import itemgetter, attrgetter
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for each in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr = sorted(arr, key = itemgetter(k))

    for eachItem in arr:
        print (*eachItem)