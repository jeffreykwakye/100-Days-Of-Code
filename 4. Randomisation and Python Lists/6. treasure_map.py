"""
A program that marks a spot with an X. 
The program should allow you to enter the position 
of the treasure using a two-digit system. The first 
digit is the vertical column number and the second 
digit is the horizontal row number. 
eg: column 2, row 3 = 23
"""

print("Specify the column and row numbers to mark X")
row_1 = ['O', 'O', 'O']
row_2 = ['O', 'O', 'O']
row_3 = ['O', 'O', 'O']
map_x = [row_1, row_2, row_3]

rows = print(f"{row_1}\n{row_2}\n{row_3}")

mark_x = input("Enter column and row number: ")

column_number = int(mark_x[0]) - 1
row_number = int(mark_x[1]) - 1

map_x[row_number][column_number] = "X"

# Amateur Hour...
# if row_number == 0: 
#     row_1[column_number] = "X"
# elif row_number == 1: 
#     row_2[column_number] = "X"
# elif row_number == 2: 
#     row_3[column_number] = "X"

print(f"{row_1}\n{row_2}\n{row_3}")



