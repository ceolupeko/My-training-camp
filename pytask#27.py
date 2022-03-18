# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

try:
    user_num = int(input("Your positive integer: "))

    # Boolean block to find root and compare with the same integer
    if user_num ** 0.5 == int(user_num ** 0.5):
        print(True)

    else:
        print(False)

except ValueError:
    print("It's not integer...")

except TypeError:
    print("It's not positive integer...")
