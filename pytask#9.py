# Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# There is one issue i couldn't solve
# if you want to see it just enter any values for list
# and after that set the target value

# User input
number_list = list(input("Your numbers: ").split())
num = input("Your number: ")

# Cycle for searching position and output
for index in range(len(number_list)):
    if number_list[index] >= num:
        print(index)
        exit()

# Output, if found no position
print(len(number_list))
