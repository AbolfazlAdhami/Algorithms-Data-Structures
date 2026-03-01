def fibonacci_head(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_head(n-1) + fibonacci_head(n-2)


print(fibonacci_head(23))
