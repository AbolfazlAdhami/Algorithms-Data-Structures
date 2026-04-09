def solve_recursive(k, n, s, f):
    m = k+1
    while m <= n and s[m] < f[k]:
        m += 1
    if m > n:
        return []
    else:
        return [m]+solve_recursive(m, n, s, f)


def solve_recursive_pro(k, n, s, f):
    m = k+1
    while m <= n and s[m] < f[k]:
        m += 1
    if m > n:
        return []
    else:
        return [m] + solve_recursive_pro(m, n, s, f)

def solve(k,n,s,f):
        activity=[]
        finish=0
        
        for k in range(1,n+1):
                if finish <=s[k]:
                        activity+=[k]
                        finish=f[k]
        return activity


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: (x[1], x[0]))

S = [0]+[A[i][0] for i in range(N)]
F = [0]+[A[i][1] for i in range(N)]

solution = solve_recursive(0, N, S, F)
print(len(solution))

for i in solution:
    print(S[i], F[i])
