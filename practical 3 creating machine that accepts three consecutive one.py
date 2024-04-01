# Aim:- Design a Program for creating machine that accepts three consecutive one.

f = 0
n = input("Enter no:")
print(n)

for j in range(len(n) - 2):
    if n[j] == '1' and n[j] == n[j + 1] and n[j + 1] == n[j + 2]:
        f = 1

if f == 1:
    print("String Accepted...")
else:
    print("String not Accepted...")
