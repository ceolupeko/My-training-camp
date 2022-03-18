# Demonstration of quick sorting in the best way O(n log n)
# But with other values in list it can be O(n ** 2)


def my_quicksort(nums) -> list[int]:
    if len(nums) < 2:
        return nums

    else:
        # Finding subsequences and pivot number
        pivot_val: int = nums[0]
        small_vals: list[int] = [num for num in nums[1:] if num <= pivot_val]
        great_vals: list[int] = [num for num in nums[1:] if num > pivot_val]

        return my_quicksort(small_vals) + [pivot_val] + my_quicksort(great_vals)


nums_in = [10, 5, 2, 3]

print(my_quicksort(nums_in))
