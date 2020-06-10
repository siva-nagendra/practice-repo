#!/Anaconda3/ python
"""
Task
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

if __name__ == "__main__":
    A, a = int(input()), set(input().split())
    N= int(input())
    n = {}
    for each in range(N):
        m1 = input()
        n1 = input().split()
        n[m1] = n1
    print (n)
    for op, se in n.items():
        print (op, se)
        if op == "intersection_update *":
            se.intersection_update(a)
    print (a)
    



