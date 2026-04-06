# def solve(n):
#         dp=[0,1,2]+[0]*(n-2)
        
#         if n > 2:
#                 for i in range(3,n+1):
#                         dp[i]=(dp[i-1]+dp[i-2])%10007
#         return dp[n]

dp={1:1,2:2}
def solve(n):
        if n not in dp:
                dp[n]=(solve(n-1)+solve(n-1))%10007
        return dp[n]
        


N =int(input())
print(solve(N))