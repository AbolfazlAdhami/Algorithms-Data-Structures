from collections import defaultdict, deque


def recover_secret(triplets):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    for triplet in triplets:
        for i in range(3):
            if triplet[i] not in in_degree:
                in_degree[triplet[i]] = 0
        for i in range(2):
            if triplet[i+1] not in graph[triplet[i]]:
                graph[triplet[i]].add(triplet[i+1])
                in_degree[triplet[i+1]] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    secret = []

    while queue:
        node = queue.popleft()
        secret.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(secret)


print(recover_secret([
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 't']
])
)
