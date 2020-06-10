#!/Anaconda3/ python
"""
Task
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
You are required to sort the data based on the the K attribute and print the final resulting table
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

N, n = int(input()), input().split()
print (all([int(i)>0 for i in n]) and any([j == j [::-1]for j in n]))