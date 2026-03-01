"""
return a largest number of a list and index of that:
10 20 30 40 50    50 , 4 
99 0 12 1          99 ,0


"""


def solve(N, S):
    maxn, maxi = S[0], 0
    for i in range(1, N):
        if maxn < S[i]:
            maxn, maxi = S[i], i
    return maxn, maxi


N = int(input())
S = list(map(int, input().split()))

maxn, maxi = solve(N, S)
print(maxn, maxi)
