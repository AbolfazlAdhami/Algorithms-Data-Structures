def sort(n, s):
    odd, even = [], []
    for i in range(n):
        if s[i] % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    odd.sort()
    even.sort()
    print(' '.join(map(str, odd)))
    print(' '.join(map(str, even)))


N = int(input())
S = list(map(int, input().split()))
sort(N, S)
