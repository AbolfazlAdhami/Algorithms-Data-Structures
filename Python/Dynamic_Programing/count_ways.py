"""
Your friend has discovered an old machine that performs simple mathematical operations. The machine has only two buttons:

+1 — adds one to the current number.

x2 — multiplies the current number by two.

The machine starts with the number 1. Now, your friend wants to know how many different ways it is possible to obtain a given number n using these buttons. Help them write a program that calculates this number.

Constraint: 1 ≤ n ≤ 10**6

Link:https://www.codewars.com/kata/67752b76d193b9d3d942bcc3/train/python
"""


def count_ways(n: int) -> int:
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] += dp[i-1]
        if i % 2 == 0:
            dp[i] += dp[i//2]
    return dp[n]


print(count_ways(1))
print(count_ways(2))
print(count_ways(3))
