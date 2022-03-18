# Power of Two
# https://leetcode.com/problems/power-of-two

# For catching wrong value
try:
    user_input_num = int(input("Your number: "))

    # For definition the result
    if user_input_num & (user_input_num - 1):
        print(False)

    else:
        print(True)

except ValueError:
    print("It's not number...")
