"""
A program that finds the highest score / number from a list.
eg: student_scores = [78, 65, 89, 86, 55, 91, 64, 89] 

// highest score should be 91

NB: You can't use either min or max functions.
"""

student_scores = input("Enter the scores here separated by a comma and space: ").split(", ")

max_score = 0
for student_score in student_scores: 
    if float(student_score) >= max_score: 
        max_score = (float(student_score))

print(f"The highest score in the class is: {max_score}")
