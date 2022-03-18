# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# User input and setting all the variables
values_list = list(input("Your values: ").split())
all_unique_values = 0

# Cycle for finding the unique values
for num in set(values_list):

    # Counting the unique values in input list
    unique_values = values_list.count(num)

    # Finding the difference
    unique_values -= 1

    # Adding quantity of unique values to the common score
    all_unique_values += unique_values

# User sorted and without duplicates list, and result output
print("------------")
print("Your sorted and without duplicates list:", sorted(set(values_list)))
print("Quantity of all the duplicates:", all_unique_values)
