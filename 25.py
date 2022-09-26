# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

values = [1, 5, 8, 3]

value = input("Enter the value")
if value in values:
    print(True)
else:
    print(False)
