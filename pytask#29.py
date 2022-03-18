# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

user_string = list(input("Your string: "))

# First unique value index output
for value in user_string:
    if user_string.count(value) == 1:
        print(user_string.index(value))
        quit()

print(-1)
