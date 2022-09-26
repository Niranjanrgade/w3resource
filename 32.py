# Write a Python program to get the least common multiple (LCM) of two positive integers.

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

min_num = min(num_1, num_2)
max_num = max(num_1, num_2)

LCM = min_num * max_num

for number in range(2, LCM):
    if number % min_num == 0 and number % max_num == 0:
        LCM = number
        break

print(LCM)