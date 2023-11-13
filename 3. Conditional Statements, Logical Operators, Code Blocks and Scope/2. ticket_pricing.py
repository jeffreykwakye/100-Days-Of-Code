"""
We are selling tickets at an amusement park, 
which I have never been to. Let's have fun with 
it though.
"""
# Heights we allow on our rides are 120cm and above. 
# Prices range from $5 - $12
# The user's age is used to determine the price they will pay.

height = float(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("How old are you please: "))

    if age < 12:
        print("Please pay $5. Thank you")
    elif age <= 18:
        print("Please pay $7. Thank you")
    else: 
        print("Please pay $12. Thank you")
else: 
    print("Sorry but you are not tall enough yet to be on this ride.")