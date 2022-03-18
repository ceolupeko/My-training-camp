# Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# I'm sorry for names of the vars and func, it's from LeetCode task :)

# Checking matches and adding to result list
def fizz_buzz() -> None:
    res: list[str] = []
    for num in range(user_num + 1):
        if num == 0:
            pass

        elif num / 3 == 5:
            res.append("FizzBuzz")

        elif num % 3 == 0:
            res.append("Fizz")

        elif num % 5 == 0:
            res.append("Buzz")

        else:
            res.append(str(num))

    print(res)


user_num = int(input("Your integer: "))

fizz_buzz()
