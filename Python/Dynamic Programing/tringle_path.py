def solve(n,t):
        dp=[[0]* (i+1) for i in range(n)]
        
        for i in range(n):
                dp[n-1][i] = t[n-1][i]
        for i in range(n-2,-1,-1):
                for j in range(i+1):
                        dp[i][j]=t[i][j] + max(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]

N=int(input())
T=[list(map(int,input().split())) for _ in range(N)]

print(solve(N,T))