import sys
sys.setrecursionlimit(10**6)


def solve(n):
    dp = [0, 0, 1, 1]+[0]*(n-3)

    for i in range(4, n+1):
        dp[i] = 1+dp[i-1]
        if i % 3 == 0:
            dp[i] = min(dp[i], 1+dp[i//3])
        if i % 2 == 0:
            dp[i] = min(dp[i], 1+dp[i//2])
    return dp[n]


dp = {1: 0, 2: 1, 3: 1}


def solve_pro(n):
    if n not in dp:
        dp[n] = 1+solve(n-1)
        if n % 3 == 0:
            dp[n] = min(dp[n], 1+solve_pro(n//3))
        if n % 2 == 0:
            dp[n] = min(dp[n], 1+solve_pro(n//2))

    return dp[n]


N = int(input())
print(solve_pro(N))
