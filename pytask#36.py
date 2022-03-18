# Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

user_string = input("Your string: ").split()
words: list[str] = []

# Every word reversing
for word in user_string:
    rev_word: list[str] = list(word[:: -1])
    words.append("".join(rev_word))

print(" ".join(words))
