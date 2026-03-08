def sorting(n, s):
    count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                count += 1
    return (s, count)


N = int(input())
S = list(map(int, input().split()))
print(sorting(N, S))
