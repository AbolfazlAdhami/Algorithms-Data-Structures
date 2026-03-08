def sort(s):
        count=0
        for i in range(1,len(s)):
                j,val=i-1,s[i]
                count+=1
                while j >=0 and s[j]>val:
                        s[j+1]=s[j]
                        j-=1
                        count+=1
                s[j+1]=val
        return (count,s)




S=list(map(int,input().split()))
print(sort(S))