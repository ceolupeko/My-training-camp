# Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

# Importing a necessary library
import roman

# Block try\except for the errors and exceptions
try:

    # User input
    number = int(input("Your integer: "))

    # Converting integer
    roman_number = roman.toRoman(number)

    # Program output
    print(roman_number)

except (ValueError, roman.OutOfRangeError):

    # Exception handling
    print("We couldn't convert that...")
