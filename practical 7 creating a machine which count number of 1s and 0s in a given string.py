# Aim:- Design a program for creating a machine which count number of 1’s and 0’s in a given string.

str_input = input("Enter a string: ")
count_1 = 0
count_0 = 0
for char in str_input:
    if char == '1':
        count_1 += 1
    elif char == '0':
        count_0 += 1
print(f"Number of 1s: {count_1}")
print(f"Number of 0s: {count_0}")
