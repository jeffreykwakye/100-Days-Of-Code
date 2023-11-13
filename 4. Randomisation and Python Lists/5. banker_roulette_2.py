"""
A program which will select a random name 
from a list of names. The person selected  
will have to pay for everybody's food bill. 

NB: You cannot use the choice() function.
"""
import random

print("Let's see who pays our bill tonight.") 
print('Enter "start" after you add the last name')
print('Enter "quit" to terminate the program')

user_names = []

while True:
    potential_payer = input("Enter a name to add to the roulette: ").lower()

    if potential_payer == "start":
        total_names = len(potential_payer)
        roulette_counter = random.randint(0, total_names - 1)

        print(f"{user_names[roulette_counter].upper()} has to pay the full bill.")
    elif potential_payer == "quit":
        break
    else:
        user_names.append(potential_payer)
