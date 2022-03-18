# Combination Sum
# https://leetcode.com/problems/combination-sum/
# I know it's not fully right solution

# Block try/except to filter not integers
try:

    # User input
    numbers = list(input("Your numbers: ").split())
    target_num = int(input("Your target number: "))

    # Cycle for summing couples of the numbers and result output
    for first_val in numbers:
        for second_val in numbers:
            if int(first_val) + int(second_val) == target_num:
                print(f"{[int(first_val), int(second_val)]}")

except ValueError:
    print("Your input values are not integers...")
