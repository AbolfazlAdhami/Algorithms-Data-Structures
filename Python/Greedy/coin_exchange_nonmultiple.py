def solve(k,coins):
        INF = k+1
        dp=[0]+ [INF]*k
        path=[[]for _ in range(k+1)]
        
        for i in range(1,k+1):
                for j in coins:
                        if j <=k and dp[i] > dp[i-j]+1:
                                dp[i]=dp[i-j]+1
                                path[i]=path[i-j]+[j]
        return dp[k],path[k]


K = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

opt, change = solve(K, coins)

print(opt)
print(*sorted(change))
