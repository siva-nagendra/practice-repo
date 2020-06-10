#!/Anaconda3/ python
"""
Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

if __name__ == "__main__":
    N,n = int(input()), set(input().split())
    M,m = int(input()), input().split()
    print (len(n.intersection(m)))