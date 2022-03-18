# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# Block try/except to filter non-sentences and non-words
try:

    # User input
    sentence = list(input("Your sentence: ").split())

    # Counting length of the last word and result output
    print(len(sentence[-1]))

except IndexError:
    print("It's not the sentence or a word...")
