# Simple summing with recursion in O(n)
# And counting the elements with recursion O(n)


def my_sum(nums, n=0) -> int:
    if n == len(nums):
        return 0

    else:
        return nums[n] + my_sum(nums, n + 1)


def my_length(nums) -> int:
    if not nums:
        return 0

    else:
        return 1 + my_length(nums[1:])


nums_in = [2, 4, 6]

print("Sum of elements:", my_sum(nums_in))
print("Quantity of elements:", my_length(nums_in))
