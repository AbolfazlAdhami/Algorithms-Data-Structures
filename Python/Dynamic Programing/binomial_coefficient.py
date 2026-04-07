def solve(n, k):
    B = [[0]*(i+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(i+1):
            if j == 0 or i == j:
                B[i][j] = 1
            else:
                B[i][j] = (B[i-1][j] + B[i-1][j-1]) % 10007
    return B[n][k]


def solve_pro(n, k):
        B = [[0]*(min(i,k)+1) for i in range(n+1)]
        for i in range(n+1):
                for j in range(min(i,k)+1):
                        if j == 0 or i == j:
                                B[i][j]=1
                        else:
                                B[i][j]=(B[i-1][j]+B[i-1][j-1])% 10007
        return B[n][k]


import math
def solve_pro2(n,k):
        return math.comb(n,k) % 10007


N, K = map(int, input().split())
print(solve_pro2(N, K))
