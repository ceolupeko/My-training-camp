# Is Subsequence
# https://leetcode.com/problems/is-subsequence/

first_user_string = list(input("Your first string: "))
second_user_string = list(input("Your second string: "))

diff = []
for value in second_user_string:
    if value not in first_user_string:
        diff.append(value)

# Cleaning the second string from values are not in the first
for diff_value in diff:
    second_user_string.remove(diff_value)

if first_user_string == second_user_string:
    print(True)

else:
    print(False)
