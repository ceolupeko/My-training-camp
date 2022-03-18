# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# This program return only values which were added in the second string

# User input and setting the variables
first_string = list(input("Your values: "))
second_string = list(input("Your values for difference: "))

# Cycle to filter the same values in both of strings
# and result output
for value in second_string:
    if value not in first_string:
        print(value)
