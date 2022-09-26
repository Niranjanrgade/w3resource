# Write a Python program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2.

# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_set = set()
for color in color_list_1:
    if color not in color_list_2:
        color_set.add(color)

print(color_set)

print(color_list_1.difference(color_list_2))