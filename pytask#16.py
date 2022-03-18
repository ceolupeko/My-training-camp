# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# I can't say exactly, but probably solving of this task could be easier

# Import necessary library
import re

# User input and setting all the variables
user_input = input("Your number\\string: ")
redactor = re.compile("[^a-zA-Z0-9 ]")
values = list((redactor.sub("", user_input.lower())))

# Cycle for deleting spaces in list(that's setting too)
while " " in values:
    values.remove(" ")

# Setting another variables
# and one of them is the creating of empty list for finding difference further
counter = -1
reading_list = []

# Cycle for adding values to the empty list for finding difference further
for iteration in range(len(values)):
    reading_list.append(values[counter])
    counter -= 1

# Block if/else for result output
if "".join(values) == "".join(reading_list):
    print("Your number\\string is Palindrome"
          "(or maybe your input was without numbers or string values)")

else:
    print("Your number\\string is not Palindrome")
