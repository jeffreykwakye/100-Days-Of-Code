"""
A short program that receives the user's age and 
shows you how long you have lived on earth in 
years, months, weeks and days (maybe) and then shows you 
how long you have left to live. Our checkout age is 90. 
***So you will be old and grey :)***
"""
# NB: 1 year = 12 months = 52 weeks = 365 days

base_age = 90 
base_age_in_months = base_age * 12
base_age_in_weeks = base_age * 52 
base_age_in_days = base_age * 365

user_age = int(input("Enter your age and we will show you how long you have been here: "))

age_in_months = user_age * 12 
age_in_weeks = user_age * 52 
age_in_days = user_age * 365 

age_in_years_left = base_age - user_age
age_in_months_left = base_age_in_months - age_in_months
age_in_weeks_left = base_age_in_weeks - age_in_weeks 
age_in_days_left = base_age_in_days - age_in_days 

message_1 = f"You have lived for {user_age} years, {age_in_months} months, {age_in_weeks} weeks and {age_in_days} days"
message_2 = f"You have {age_in_years_left} years, {age_in_months_left} months, {age_in_weeks_left} weeks and {age_in_days_left} days left to live"

print(message_1) 
print(message_2)
