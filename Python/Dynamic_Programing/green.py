def green(n: int) -> int:
    dp = [1]
    current = 2
    while len(dp) < n:
        length = len(str(current))
        modulus = 10 ** length
        if (current ** 2) % modulus == current:
            dp.append(current)
        current += 1
    return dp[n - 1]


print(green(4))
print(green(12))
# print(green(13))
# print(green(100))

"""
This is a very simply formulated task. Let's call an integer number N 'green' if N² ends with all of the digits of N. Some examples:

5 is green, because 5² = 25 and 25 ends with 5.

11 is not green, because 11² = 121 and 121 does not end with 11.

376 is green, because 376² = 141376 and 141376 ends with 376.

Your task is to write a function green that returns the nth green number, starting with 1 - green (1) == 1

Input range
n <= 5000

"""
