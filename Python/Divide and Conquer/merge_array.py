def merge(n,m,a,b):
        c = [0] *(n+m)
        i = j = k = 0
        
        while i < n and j < m:
                if a[i] < b[j]:
                        c[k] = a[i]; i+=1;k+=1
                        i+=1
                else:
                        c[k] = b[j]; j+=1;k+=1
        while i < n: c[k] = a[i]; i+=1;k+=1
        while j < m: c[k] = b[j]; j+=1;k+=1
        return c

def solve():
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        c = merge(n,m,a,b)
        print(*c)