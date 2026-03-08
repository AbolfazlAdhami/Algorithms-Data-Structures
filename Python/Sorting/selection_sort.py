def sort(n,s):
        count=0
        
        for i in range(n-1):
                minv,minj=s[i],i
                for j in range(i+1,n):
                        if s[j]<minv:
                                minv,minj=s[j],j
                        if i != minj:
                                s[i],s[minj]=s[minj],s[i]
                                count+=1
        return (s,count)


N=int(input())
S=list(map(int,input().split()))
print(sort(N,S))