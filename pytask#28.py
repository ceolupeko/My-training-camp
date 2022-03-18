# Ransom Note
# https://leetcode.com/problems/ransom-note/
# I'm sorry for names of the variables, it's from LeetCode task :)

# Checking consisting one values in other
def ransom():
    if ransomNote in magazine:
        print(True)

    else:
        print(False)


ransomNote = input("Your values for ""ransomNote"""
                   "(only lowercase letters): ")
magazine = input("Your values for ""magazine"""
                 "(only lowercase letters): ")

if ransomNote.isalpha() and magazine.isalpha():
    if ransomNote.islower():
        ransom()

    else:
        print("It's not lowercase letters...")

else:
    print("It's not the letters...")
