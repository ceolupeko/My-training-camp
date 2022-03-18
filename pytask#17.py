# Single Number
# https://leetcode.com/problems/single-number/

# User input values and converting them to list
user_input_values = list(input("Your values: ").split())

# Cycle for determining the result and its output
for value in user_input_values:
    if user_input_values.count(value) == 1:
        print(value)
