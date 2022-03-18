# Move Zeroes
# https://leetcode.com/problems/move-zeroes/

user_values = input("Your integers(separated by a space): ").split()

try:
    nums = [int(num) for num in user_values]

except ValueError:
    print("It's not integers...")

else:
    zeros_quantity = nums.count(0)

    while 0 in nums:
        nums.remove(0)

    sorted_nums = sorted(nums)

    # Adding previously deleted zeros in the end of already sorted list
    for iterations in range(zeros_quantity):
        sorted_nums.append(0)

    print(sorted_nums)
