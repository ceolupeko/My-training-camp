# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Importing a necessary library
import roman

# Block try\except for the errors and exceptions
try:

    # User input
    roman_number = input("Your roman number: ")

    # Converting roman number
    number = roman.fromRoman(roman_number)

    # Program output
    print(number)

except (ValueError, roman.InvalidRomanNumeralError):

    # Exception handling
    print("We couldn't convert that...")
