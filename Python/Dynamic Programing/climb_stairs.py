# def solve(n, a):
#     dp = [0]*(n+1)
#     dp[1] = a[1]

#     for i in range(2, n+1):
#         dp[i] = a[i]+max(dp[i-1], dp[i-2])
#     return dp[n]
dp={0:0}

def solve(n, a):
        if n==1:
                dp[n]=a[n]
        elif n not in dp:
                dp[n]=a[n]+max(solve(n-1,a),solve(n-2,a))
        return dp[n]


N = int(input())
A = [0] + list(map(int, input().split()))
print(solve(N,A))
