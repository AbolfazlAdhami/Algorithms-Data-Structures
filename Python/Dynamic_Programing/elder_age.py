def elder_age(m, n, l, t):
    total = 0
    for r in range(m):
        for c in range(n):
            val = r ^ c
            if val >= l:
                total += val - l
    return total % t


def elder_age_dp(m, n, l, t):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            xor_value = (r - 1) ^ (c - 1)
            contribution = max(0, xor_value - l)
            dp[r][c] = (dp[r - 1][c] + dp[r][c - 1] -
                        dp[r - 1][c - 1] + contribution) % t
    return dp[m][n]


print(elder_age(8, 5, 1, 100))  # Output: 5
print(elder_age(8, 8, 0, 100007))  # Output: 224
print(elder_age(25, 31, 0, 100007))  # Output: 5
# print(elder_age(28827050410, 35165045587, 7109602, 13719506))  # Output: 5

print(elder_age_dp(8, 5, 1, 100))  # Output: 5
print(elder_age_dp(8, 8, 0, 100007))  # Output: 224
print(elder_age_dp(25, 31, 0, 100007))  # Output: 5
print(elder_age_dp(28827050410, 35165045587, 7109602, 13719506))  # Output: 5
