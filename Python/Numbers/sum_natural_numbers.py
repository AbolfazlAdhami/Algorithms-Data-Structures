def sum(N):
    s = 0
    for i in range(1, N+1):
        s += i
    return s


N = int(input())
print(sum(N))


def sum_rec(N):
    s = 1
    if N >= 2:
        return N + sum_rec(N-1)
    return s


N = int(input())
print(sum_rec(N))
