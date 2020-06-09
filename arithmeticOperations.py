#!C/Users/siva_/Anaconda3/ python
"""
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a + b)
    print (a - b)
    print (a * b)