# Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# I know i should solve this with any algo,
# but i ain't looking for the hard ways

# Import necessary library
import math

# Block try/except to filter non-integer
try:

    # User input
    number = int(input("Your number: "))

    # Result output
    print(int(math.sqrt(number)))

except ValueError:
    print("It's not number...")
