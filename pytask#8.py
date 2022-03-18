# Remove Element
# https://leetcode.com/problems/remove-element/

# User input
values_list = list(input("Your values: ").split())
value = input("Your value: ")

# Cycle for removing all the instances of value you entered
while value in values_list:
    values_list.remove(value)

# All info and result output
print("---------------")
print("Length of the new list:", len(values_list))
print("Your list without value you entered:", values_list)
