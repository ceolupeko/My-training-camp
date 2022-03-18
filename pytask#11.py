# Permutations
# https://leetcode.com/problems/permutations/

# Importing necessary libraries
from itertools import permutations

# User input and setting a variable
user_list = list(input("Your values: ").split())
set_user_list = set(user_list)

# Block if/else for filter not unique user values and result output
if len(user_list) == len(set_user_list):
    print(list(permutations(user_list)))

else:
    print("Your values are not unique")
