# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# User input to list
first_user_input = list(input("Your phrase: "))
second_user_input = list(input("Your second phrase: "))

# Boolean block to comparing, and result output
if sorted(first_user_input) == sorted(second_user_input):
    print(True)

else:
    print(False)
