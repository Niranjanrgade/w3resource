# Write a Python program to create a histogram from a given list of integers.
list_of_integers = []


def input_function():
    while True:
        input_text = input("Enter any number to add in list OR press other than number to exit: ")
        if input_text.isdigit():
            list_of_integers.append(input_text)
        else:
            break


def histogram(list_of_integers):
    for integer in list_of_integers:
        integer = int(integer)
        print(str(integer) + ':' + "#" * integer)


input_function()
histogram(list_of_integers)
