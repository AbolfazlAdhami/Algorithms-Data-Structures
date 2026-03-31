def partition(low, high, s):
        pivot = s[high]
        i = low 
        
        for j in range(low+1, high+1):
                if s[j] < pivot:
                        i+=1
                        s[i],s[j]=s[j],s[i]
        s[low],s[i]=s[i],s[low]
        return i

N,L,H=map(int,input().split())
S=list(map(int,input().split()))
pivot_index = partition(L,H,S)
print(pivot_index)
print(*S)