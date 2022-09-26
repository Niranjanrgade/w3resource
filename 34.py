# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

num_1 = int(input("1: "))
num_2 = int(input("2: "))

if 15 <= num_1 + num_2 <= 20:
    print(20)
else:
    print(num_1 + num_2)