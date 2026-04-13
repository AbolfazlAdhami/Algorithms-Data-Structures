class Item:
    def __init__(self, weight, profit) -> None:
        self.weight = weight
        self.profit = profit


def solve(W, items):
    # Sort items by value density (profit/weight) in descending order
    items.sort(key=lambda x: (x.profit / x.weight), reverse=True)

    opt = 0.0  # Use float for precision in fractional knapsack
    for i in items:
        if i.weight <= W:
            W -= i.weight
            opt += i.profit
        else:
            # Take the fraction that fits
            opt += i.profit * (W / i.weight)
            break
    return opt


# Reading input
N, W = map(int, input().split())
weights = [*map(int, input().split())]
profits = [*map(int, input().split())]

items = [Item(w, p) for w, p in zip(weights, profits)]
print(solve(W, items))
