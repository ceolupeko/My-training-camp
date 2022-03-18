# Demonstration of finding smallest number, and selection sort


# Passing all nums list in O(n ** 2)
def finding_smallest(nums) -> int:
    smallest_num: int = nums[0]
    smallest_num_index = 0
    for index in range(1, len(nums)):
        if nums[index] < smallest_num:
            smallest_num = nums[index]
            smallest_num_index = index

    return smallest_num_index


# Adding sorted nums to the new list in O(n ** 2) too
def sorting(nums) -> list[int]:
    sorted_nums = []
    for iterations in range(len(nums)):
        min_num: int = finding_smallest(nums)
        sorted_nums.append(nums.pop(min_num))

    return sorted_nums


nums_in = [5, 3, 6, 2, 10]

print(sorting(nums_in))
