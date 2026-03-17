def fibonacci_memorization(n, table):
    if n not in table:
        table[n] = fibonacci_memorization(
            n-1, table) + fibonacci_memorization(n-2, table)

    return table[n]


def fibonacci_tabulation(n,table):
        for i in range(2,n+1):
                table[i]=table[i-1] + table[i-2]

        return table[n]

t = {0: 0, 1: 1}


print(fibonacci_memorization(100,t))
print(fibonacci_tabulation(500,t))