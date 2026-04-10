def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(p, q):
    if q < q:
        parent[q] = p
    else:
        parent[p] = q


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    x, a, b = map(int, input().split())
    p = find(a)
    q = find(b)

    if x == 1:
        union(p, q)
    if x == 2:
        print("Yes" if p == q else "No")

"""
7 8  
1 1 3
2 1 7   
No
1 7 6
2 7 1
No
1 3 7
1 4 2
1 1 1
2 1 1
Yes

"""
