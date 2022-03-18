# Palindrome Number\String
# https://leetcode.com/problems/palindrome-number/

# Setting all the variables
values = list(input("Your number\\string: "))
counter = -1
reading_list = []

# Passing number\string from the end and adding to another list
for iteration in range(len(values)):
    reading_list.append(values[counter])
    counter -= 1

# Block if\else to definition the result
if "".join(reading_list) == "".join(values):
    print("Your number\\string is Palindrome")

else:
    print("Your number\\string is not Palindrome")
