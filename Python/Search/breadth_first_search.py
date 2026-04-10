def bfs(graph,s,visited):
        queue=[]
        queue.append(s)
        
        vstate = [False] * (N+1)
        vstate[s]=True
        
        while queue:
                u=queue.pop(0)
                for v in sorted(graph[u]):
                        if not vstate[v]:
                                queue.append(v)
                                vstate[v]=True
                                visited.append(v)


N, M, S = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = []
bfs(graph,S,visited) 
print(*visited)
