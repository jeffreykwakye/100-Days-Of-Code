"""
A program that calculates the average student height 
from a List of heights. 

eg: student_heights = [180, 124, 165, 173, 189, 169, 146]. 
The average height can be calculated by adding all the heights 
together and dividing by the total number of heights. 

NB: WE CAN'T USE THE SUM OR LEN FUNCTIONS....GREAT.
"""

student_heights = input("Enter the student heights. Please separate them with a comma: ").split(", ")

height_count = 0
height_sum = 0

for student_height in student_heights: 
    height_count += 1


for student_height in student_heights: 
    height_sum += float(student_height)

average_height = round(height_sum / height_count)

print(average_height)




# for cleaned_height in cleaned_heights:
#     student_heights.append(float(cleaned_height))

# average_height = sum(student_heights) / len(student_heights)

# print(f"Average Height 1: {round(average_height)}")

# # #####################################################

# total_heights = 0;
# heights_count = len(student_heights)
# for student_height in student_heights:
#     total_heights += student_height 

# average_height_2 = total_heights / heights_count

# print(f"Average height 2: {round(average_height_2)}")