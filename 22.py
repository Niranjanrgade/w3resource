# Write a Python program to count the number 4 in a given list.

input_text = input("Enter anything: ")

count = 0

for character in input_text:
    if character == '4':
        count += 1

print(count)
