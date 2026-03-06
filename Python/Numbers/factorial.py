def fact(n):
    result = 1
    while n != 0:
        result *= n
        n -= 1
    return result


n = int(input())

print(fact(n))
