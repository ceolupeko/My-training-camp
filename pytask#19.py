# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# User input values for list
user_input_list = input("Your values: ").split()

# Boolean block to compare user list & filtered one, and result output
if len(user_input_list) != len(set(user_input_list)):
    print(True)

else:
    print(False)
