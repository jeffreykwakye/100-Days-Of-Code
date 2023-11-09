"""
A tip calculator to help those who tip (not me) to know 
exactly how much tip they should give. 
NB: We will not be using loops or any of the cool stuff in 
python.  
Get it done!!!
"""

print("Welcome to the tip calculator")

bill = float(input("What is the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_between = int(input("How many people to split the bill? "))

tip_actual = bill * (tip_percentage / 100) 
total_bill = bill + tip_actual

bill_per_person = total_bill / split_between

message_1 = f"The total bill including {tip_percentage}% tip is ${round(total_bill, 2)}"
message_2 = f"Each person should pay: {'{:.2f}'.format(bill_per_person)}"

print(message_1 + "\n")
print(message_2)