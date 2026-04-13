from heapq import heappop, heappush

INF = 10**9


def dijkstra(s):
    dist = [INF] * (N + 1)
    dist[s] = 0
    visited = [False] * (N + 1)

    pq = [(0, s)]

    while pq:
        d, u = heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for w, v in graph[u]:
            cost = d + w
            if dist[v] > cost:
                dist[v] = cost
                heappush(pq, (cost, v))

    return dist


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dist = dijkstra(1)

for i in range(1, N + 1):
    print(dist[i] if dist[i] < INF else -1)
