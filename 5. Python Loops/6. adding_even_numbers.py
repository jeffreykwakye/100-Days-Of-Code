"""
A program that sums all the even numbers 
between 1 and 100 inclusive. 

NB: Use the range() function and there should 
be just one output.  
"""

total = 0
for number in range(0, 101, 2):
    total += number
print(total)

total_2 = 0
for number in range (1, 101):
    if number % 2 == 0:
        total_2 += number
print(total_2)