"""
A program receives a number from the user and then 
works out whether a given number is an odd or even number 
Hint: Even numbers can be divided by 2 with no 
remainder. eg. 4 / 2 = 2, remainder 0
"""
print("We will tell you whether your number is even or odd")
user_number = float(input("Enter your number here: "))

if user_number % 2 == 0:
    print(f"{user_number} is an even number")
else:
    print(f"{user_number} is an odd number")