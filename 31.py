# Write a Python program to compute the greatest common divisor (GCD) of two positive integers

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

min_num = min(num_1, num_2)
max_num = max(num_1, num_2)

GCD = 1
if max_num % min_num == 0:
    GCD = min_num
else:
    for number in range(min_num, 0, -1):
        if num_1 % number == 0 and num_2 % number == 0:
            GCD = number
            break

print(GCD)



