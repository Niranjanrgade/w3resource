# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

input_string = input("Enter a string: ")
n = int(input("Enter the n value: "))


def copier(input_string, n):

    if len(input_string) < 2:
        return n * input_string

    else:
        return input_string[:2] * n + input_string[2:]


print(copier(input_string, n))

