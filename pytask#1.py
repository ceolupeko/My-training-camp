# Detect Capital
# https://leetcode.com/problems/detect-capital/

# User input
input_word = input("Your word is: ")

# if/else block to filter out wrong word length
if 1 <= len(input_word) <= 100:
    input_word.isupper()

else:
    print("Wrong length of word...")
