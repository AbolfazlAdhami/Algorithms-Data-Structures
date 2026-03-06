def median(s):
    s.sort()
    while len(s) > 0:
        mid = (len(s)-1)//2
        print(s, mid, s[mid])
        s.remove(s[mid])
    print()


N = int(input())
S = list(map(int, input().split()))
median(S)
