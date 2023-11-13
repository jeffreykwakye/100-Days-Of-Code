"""
This program is an updated BMI Calculator. 
Well now we will tell you whether you are underweight, 
normal weight, overweight, obese or clinically obese. 

NB: < 18.5 = underweight, 
    > 18.5 < 25 = normal weight 
    > 25 < 30 = overweight 
    > 30 < 35 = obese 
    > 35 = clinically obese. 
"""

user_height = float(input("Please enter your height in meters (m): "))
user_weight = float(input("Please enter your weight in kilograms (kg): "))

user_bmi = user_weight / (user_height ** 2)
message = ""

if user_bmi < 18.5: 
    message = f"Your BMI is {round(user_bmi)}. You are underweight" 
elif user_bmi <= 25: 
    message = f"Your BMI is {round(user_bmi)}. You have a normal weight"
elif user_bmi <= 30: 
    message = f"Your BMI is {round(user_bmi)}. You are overweight"
elif user_bmi <= 35:
    message = f"Your BMI is {round(user_bmi)}. You are obese"
else:
    message = f"Your BMI is {round(user_bmi)}. You are clinically obese"
    
print(message)