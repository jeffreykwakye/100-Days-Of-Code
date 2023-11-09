"""
Write a program that adds the digits in a 2 digit number eg if the input was 35, 
then the output should be 3 + 5 = 8. 
All this is to be done without using loops.
"""

user_number = input("Give us two numbers to add up\n")

number_1 = int(user_number[0])
number_2 = int(user_number[1])
number_sum = number_1 + number_2

print("The sum of the numbers is " + str(number_sum) + "." )

