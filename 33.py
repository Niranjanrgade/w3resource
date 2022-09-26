# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

num_1 = int(input("Enter integer: "))
num_2 = int(input("Enter integer: "))
num_3 = int(input("Enter integer: "))

if num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print(0)
else:
    print(num_1 + num_2 + num_3)