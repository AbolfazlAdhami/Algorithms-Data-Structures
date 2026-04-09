def solve_recursive(k, i, coins):
    if k == 0:
        return 0, []
    else:
        if k >= coins[i]:
            opt, change = solve_recursive(k-coins[i], i, coins)
            return opt+1, change+[coins[i]]
        else:
            opt, change = solve_recursive(k, i+1, coins)
            return opt, change

def solve_pro(k,coins):
        change=[]
        for i in range(len(coins)):
                while k >=coins[i]:
                        k-=coins[i]
                        change.append(coins[i])
                if k ==0:
                        break
        return len(change) , change


def solve(k,coins):
        change=[]
        for i in range(len(coins)):
                change+=[coins[i]] * (k//coins[i])
                k = k %coins[i]
                if k == 0:
                        break
        return len(change),change


K = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

opt, change = solve(K, coins)

print(opt)
print(*sorted(change))
