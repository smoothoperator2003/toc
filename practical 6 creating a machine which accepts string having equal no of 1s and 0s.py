# Aim:- Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s.

str_input = input("Enter a string: ")
ones = 0
zeroes = 0
for i in range(len(str_input)):
    if str_input[i] == '1':
        ones += 1
    elif str_input[i] == '0':
        zeroes += 1
if ones == zeroes:
    print("String accepted")
else:
    print("String Rejected")
