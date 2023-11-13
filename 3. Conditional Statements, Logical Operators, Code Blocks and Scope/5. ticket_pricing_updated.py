"""
We are selling tickets at an amusement park, 
which I have never been to. Let's have fun with 
it though.
"""
# Heights we allow on our rides are 120cm and above. 
# Prices range from $5 - $12
# Pictures taken on rides cost $3 and it is optional.
# The user's age is used to determine the price they will pay.

bill = 0.00

height = float(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride this rollercoaster!")
    age = int(input("How old are you please: "))

    # if age >= 45 and age <= 55:
    #     print("Your ticket comes at no charge. Please enjoy the ride!")
    # else:
    if age < 12:
        print("Child tickets are $5.00")
        bill += 5
    elif age <= 18:
        print("Teen tickets are $7.00")
        bill += 7
    elif age > 18 and (not (age >= 45 and age <= 55)): 
        print("Adult tickets are $12.00")
        bill += 12
    
    print("Do you want a picture? Enter yes/y or no/n.")
    print("Please not that if you enter yes or y, you will be billed an extra $3.")
    picture_request = input("Do you want your picture taken? ").lower()

    if picture_request == "yes" or picture_request == 'y':
        bill += 3

    print(f"Please pay ${'{:.2f}'.format(bill)}")
    bill_paid = float(input("$"))

    if bill_paid == bill:
        print("Thank you. Enjoy the ride!")
    elif bill_paid > bill:
        change = bill_paid - bill 
        print(f"Your change is ${'{:.2f}'.format(change)}. Thank you and enjoy the ride!")
    else:
        print("Please pay the full bill in the next queue.")

else: 
    print("Sorry but you are not tall enough yet to be on this ride.")