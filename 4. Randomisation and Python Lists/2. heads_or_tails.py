"""
A program that simulates a virtual coin toss. 
It will randomly tell the user Heads or Tails.
Let's see if we will get heads or tails.
"""

import random 

heads_or_tails = random.randint(1, 2)
roll = ""

if heads_or_tails == 1:
    roll = "Heads"
elif heads_or_tails == 2:
    roll = "Tails"

print(roll)