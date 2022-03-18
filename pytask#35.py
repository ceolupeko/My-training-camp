# Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

user_vals: list[str] = input("Your integers(separated by space): ").split()

try:
    # Integer list from string one
    user_nums: list[int] = [int(value) for value in user_vals]

except ValueError:
    print("It's not integers...")

else:
    # Finding duplicates
    duplicates: list[int] = []
    for num in user_nums:
        if user_nums.count(num) > 1:
            duplicates.append(num)

    print(sorted(set(duplicates)))
