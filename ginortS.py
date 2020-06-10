#!/Anaconda3/ python
"""
Task
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.te and print the final resulting table
"""
__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

s = input()
print ("".join(sorted([x for x in s if x.islower()])), end = "")
print ("".join(sorted([x for x in s if x.isupper()])), end = "")
print ("".join(sorted([y for y in [x for x in s if x.isdigit()] if int(y) % 2 != 0])), end = "")
print ("".join(sorted([y for y in [x for x in s if x.isdigit()] if int(y) % 2 == 0])))