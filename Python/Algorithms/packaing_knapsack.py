class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


def solve(n, w, items, D):
    if n == 0 or w <= 0:
        return 0

    if (n, w) in D:
        return D[(n, w)]

    # Case 1: don't take item n
    not_take = solve(n-1, w, items, D)

    # Case 2: take item n (if possible)
    take = 0
    if items[n].weight <= w:
        take = items[n].profit + solve(n-1, w-items[n].weight, items, D)

    D[(n, w)] = max(not_take, take)
    return D[(n, w)]


N, W = map(int, input().split())
weights = list(map(int, input().split()))
profits = list(map(int, input().split()))

items = [None] + [Item(w, p) for w, p in zip(weights, profits)]
D = {}

print(solve(N, W, items, D))
