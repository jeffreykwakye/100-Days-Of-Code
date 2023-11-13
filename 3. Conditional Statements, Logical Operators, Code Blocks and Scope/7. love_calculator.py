"""
Errm this is a weird one. That's all I am going to say about it. 
Just don't read too much BuzzFeed else you will build something like this. 
Any way it is supposed to be a LOVE CALCULATOR. Yeah...you didn't misread it. 
So here goes.
"""
print("Welcome to the LOVE CALCULATOR!")

name_1 = input("What is your name?\n").lower()
name_2 = input("What is name of your would be love?\n").lower()

combined_name = name_1 + name_2

love_score = 0
true_counter = 0
love_counter = 0

true_counter += combined_name.count('t')
true_counter += combined_name.count('r')
true_counter += combined_name.count('u')
true_counter += combined_name.count('e')

love_counter += combined_name.count('l')
love_counter += combined_name.count('o')
love_counter += combined_name.count('v')
love_counter += combined_name.count('e')

love_score += int(str(true_counter) + str(love_counter)) 


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50: 
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}")
