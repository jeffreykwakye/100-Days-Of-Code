"""
A program to generate a password for the user. 

Name will be "PyPassword Generator"...which I think 
is weird. 
"""
import random 

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '#', '@', '$', '%', '^', '&', '*', '(', 
    ')', '_', '+', '~'
]

print("Welcome to the PyPassword Generator!")


user_letters = input("How many letters do you want?\n")
user_numbers = input("How many numbers do you want?\n")
user_symbols = input("How many symbols do you want?\n")

generated_password = []

if int(user_letters) > 0:
    for l in range (0, int(user_letters)):
        generated_password.append(letters[random.randint(0, len(letters) - 1)])

if int(user_numbers) > 0:
    for n in range(0, int(user_numbers)):
        generated_password.append(numbers[random.randint(0, len(numbers) - 1)])

if int(user_symbols) > 0:
    for n in range(0, int(user_symbols)):
        generated_password.append(symbols[random.randint(0, len(symbols) - 1)])

random.shuffle(generated_password)

password_set = ""

for gp in generated_password:
    password_set += gp

print(f"Your password length is: {len(password_set)} and your password is: {password_set}")