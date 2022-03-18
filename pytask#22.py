# Add Digits
# https://leetcode.com/problems/add-digits/

# Setting limit digits in a number
limit_value = 10

# Handling user input
try:
    num = int(input("Your integer: "))

except ValueError:
    print("It's not integer...")

# Main block of program
else:
    # Cycle to summing digits
    while num >= limit_value:
        num = (num // limit_value) + (num % limit_value)

    # Result output
    print(num)
