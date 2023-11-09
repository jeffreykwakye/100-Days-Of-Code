"""
PEMDAS(LR) is used
P = Parenthesis 
E = Exponents 
M = Multiplication 
A = Addition 
S = Subtraction
LR = Left is given precedence over right. eg. For division and multiplication, 
whichever is leftmost is calculated first. 
"""

# Example question 
# 3 * 3 + 3 / 3 - 3 
# My expected answer is 7.0 if I actually do understand this 

print(3 * 3 + 3 / 3 - 3)

# To change the order to print 3.o instead of 7.0
print(3 - 3 + 3 * 3 / 3)