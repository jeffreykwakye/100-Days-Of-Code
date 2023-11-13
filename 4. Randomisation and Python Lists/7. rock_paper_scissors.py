"""
Rock-Paper-Scissors. 
Let's build the classic game. 

Rules: 
Rock beats Scissors, 
Paper beats Rock, 
Scissors beat Paper
"""
import random

# Rock Paper Scissors ASCII Art

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

user_choice = int(input('Enter "0" for Rock, "1" for Paper or "2" for Scissors: '))
computer_choice = random.randint(0, 2)

if user_choice == computer_choice: 
    print("Draw")
elif user_choice == 0 and computer_choice == 2: 
    print(f"{rock} beats {scissors}. You win!")
elif user_choice == 1 and computer_choice == 0:
    print(f"{paper} beats {rock}. You win!")
elif user_choice == 2 and computer_choice == 1:
    print(f"{scissors} beat {paper}. You win!")
elif computer_choice == 0 and user_choice == 2: 
    print(f"{rock} beats {scissors}. You Lose!")
elif computer_choice == 1 and user_choice == 0:
    print(f"{paper} beats {rock}. You Lose!")
elif computer_choice == 2 and user_choice == 1:
    print(f"{scissors} beat {paper}. You Lose!")
else:
    print("What the hell did you select!")