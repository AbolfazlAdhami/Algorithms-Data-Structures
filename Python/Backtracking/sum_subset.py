from itertools import combinations


def solve(n,w,a):
        cnt=0
        
        for i in range(1,n+1):
                for c in combinations(a,i):
                        if sum(c)==w:
                                cnt+=1
        return cnt

# N,W=map(int,input().split())
# A=[*map(int,input().split())]
# print(solve(N,W,A))


def promising(i,weight,total):
        if weight == W:
                return True
        if weight + total < W:
                return False
        if weight + w[i+1]>W:
                return False
        return True

def sum_of_subset(i,weight,total,include):
        global cnt
        
        if promising(i,weight,total):
                
                if weight ==W:
                        cnt+=1
                else:
                        include[i+1]=True
                        sum_of_subset(i+1,\
                                weight+w[i+1],total-w[i+1],include)
                        include[i+1]=False
                        sum_of_subset(i+1,\
                                weight,total-w[i+1],include)
                        

n,W=map(int,input().split())
w=[0]+[*map(int,input().split())]
w.sort()
total=sum(w)
include=[0]*(n+1)
cnt=0
sum_of_subset(0,0,total,include)
print(cnt)
