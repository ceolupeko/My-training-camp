# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# I found i've already did this task
# I'm sorry, but you may count this version like better one

first_user_string = list(input("Your first string: "))
second_user_string = list(input("Your second string: "))

# Finding different value
for diff_value in second_user_string:
    if diff_value not in first_user_string:
        print(diff_value)
