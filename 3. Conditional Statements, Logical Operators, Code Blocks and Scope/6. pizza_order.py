"""
A pizza order program that calculates the final bill 
based on size of pizza and other toppings. 
You cannot use lists or dictionaries. So this will be  
a bit boring and long to write.

small_pizza = 15 
medium_pizza = 20 
large_pizza = 25 
"""

print("Welcome to Python Pizza Deliveries!") 
print("What size pizza do you want?\n")
print("A large size costs $25")
print("A medium size costs $20")
print("A small size costs $15\n")
print("Enter L or l for large pizza\nM or m for medium\nS or s for small\n")

pizza_size = input("Please enter the size here: ").lower()
total_bill = 0.00

if pizza_size == "l":
    total_bill += 25
elif pizza_size == "m":
    total_bill += 20
else: 
    total_bill += 15

add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()

if add_pepperoni == 'y' and pizza_size == 's':
    total_bill += 2
elif add_pepperoni == 'y' and pizza_size != 's':
    total_bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if extra_cheese == 'y':
    total_bill += 1

print(f"Your total bill is ${'{:.2f}'.format(total_bill)}")

