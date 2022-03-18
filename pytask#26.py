# Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

first_user_vals = input("Your first values(separated by a space): ").split()
second_user_vals = input("Your first values(separated by a space): ").split()

common_vals = []

# Comparing every value from lists and adding to result list
for value in first_user_vals:
    if value in second_user_vals:
        common_vals.append(value)

print(common_vals)
