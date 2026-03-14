import doctest
# Not Working for numbers


def lcs_old(x, y):
    assert x is not None
    assert y is not None
    m = len(x)
    n = len(y)
    if m == 0 or n == 0:
        return ""
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = 1 if x[i-1] == y[j-1] else 0
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+match)
    seq = ''
    while i > 0 and j > 0:
        match = 1 if x[i - 1] == y[j - 1] else 0

        if dp[i][j] == dp[i - 1][j - 1] + match:
            if match == 1:
                seq = x[i - 1] + seq
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return seq


doctest.testmod()


def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            seq.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    seq.reverse()
    return ''.join(seq)


print(lcs("abc", "ac"))  # Output: "ac"
"""
        a   b   c
    a   X 
    c           X

        DP ===> ac
"""
print(lcs("132535365", "123456789"))  # Output: "12356"
"""
        1   3   2   5   3   5   3     6    5
        
    1   X
    2           X
    3       X           X       X
    4
    5               X       X               X
    6                                 X
    7
    8
    9 
                DP =====> 12356
"""

print(lcs("", ""))  # Output: ""
