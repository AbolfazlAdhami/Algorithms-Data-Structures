def dfs(graph,v,visited):
        vstate[v]=True
        visited.append(v)
        
        for u in sorted(graph[v]):
                if not vstate[u]:
                        dfs(graph,u,visited)
                        
                        



N,M,S=map(int,input().split())
graph={i:[] for i in range(1,N+1)}

for _ in range(M):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
vstate=[False] * (N+1)
visited=[]

dfs(graph,S,visited)
print(*visited)