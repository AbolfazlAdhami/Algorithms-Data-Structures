def promising(i):
    for k in range(1, i):
        if col[i] == col[k]:
            return False
        if abs(col[i]-col[k]) == abs(i-k):
            return False
    return True


def nqueen(i):
    global cnt

    if promising(i):
        if i == N:
            cnt += 1
        else:
            for j in range(1, N+1):
                col[i+1] = j
                nqueen(i+1)


N = int(input())
col = [0]*(N+1)
cnt = 0
nqueen(0)
print(cnt)
