#!C/Users/siva_/Anaconda3/ python

"""CharacterInput.py: This lets user input their name and age and it guesses the age of that person in a random number of years."""

__author__      = "Siva Nagendra"
__copyright__   = "Copyright 2020, Planet Earth"

import random
name = input("Enter your name = ")
age = int(input("Enter your age = "))
randInt = random.randint(age + 1 , 1000)
finalAge = 2020 + randInt
print ()
print ("Hey %s, Congratulations!! You will turn %d years in %d." % (name, randInt, finalAge))