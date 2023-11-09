"""
BMI Calculator using weight in kg and height in m
The result should be a whole number not a floating point.
"""
print("This is a BMI calculator that calculates your BMI using your weight in kg and height in m")
user_height = float(input("Please enter your height in meters (m): "))
user_weight = float(input("Please enter your weight in kilograms (kg): "))

bmi = user_weight / user_height**2 

print("Your BMI is " + str(round(bmi, 2)))


