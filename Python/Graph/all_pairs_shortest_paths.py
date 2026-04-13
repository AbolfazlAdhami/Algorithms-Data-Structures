def floyd(n, W):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])


INF = 10**9

N, M = map(int, input().split())

W = [[INF] * N for _ in range(N)]

for i in range(N):
    W[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    W[u][v] = w

floyd(N, W)

for i in range(N):
    for j in range(N):
        if W[i][j] == INF:
            W[i][j] = 0
    print(*W[i])
