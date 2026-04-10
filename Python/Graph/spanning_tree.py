from heapq import heappop,heappush


def find(a):
        if a!=parent[a]:
                parent[a]=find(parent[a])
        return parent[a]

     
def union(p,q):
        if p<q:
                parent[q]=p
        else:
                parent[p]=q   
        
def kruskal(n,E):
        F=[]
        while len(F)<n-1:
                e=heappop(E)[1]
                p=find(e[0])
                q=find(e[1])
                
                if p !=q:
                        union(p,q)
                        F.append(e)
        return F
                              
        
        
        
N,M=map(int,input().split())
E=[]
for _ in range(M):
        u,v,w=map(int,input().split())
        heappush(E,(w,(u,v,w)))
parent=[i for i in range(N)]
F=kruskal(N,E)
s=0
for i in range(len(F)):
        s+=F[i][2]
print(s)
        