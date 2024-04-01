# Aim:- Design a Program for creating machine that accepts the string always ending with 101.

f = 0
n = input("Enter the string with values 0 and 1: ")
print(n)

for j in range(len(n)):
    if n[-1] == '1' and n[-2] == '0' and n[-3] == '1':
        f = 1

if f == 1:
    print("String Accepted...")
else:
    print("String not Accepted...")
