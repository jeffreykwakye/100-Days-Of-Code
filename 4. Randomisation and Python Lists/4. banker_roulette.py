"""
A program which will select a random name 
from a list of names. The person selected  
will have to pay for everybody's food bill. 

NB: You cannot use the choice() function.
"""
import random

print("Let's see who pays our bill tonight.") 
print('Please use "," to separate the names')

names = input("The names please: ")
potential_payers = names.split(", ")

roulette_choice = random.randint(0, len(potential_payers) - 1)

print(f"{potential_payers[roulette_choice]} has to pay the full bill")