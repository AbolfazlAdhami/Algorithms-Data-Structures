import time


def divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


n = int(input())
start = time.time()
print(divisors(n))
end = time.time()
print(f'solve time is {end-start}')


def divisors2(n):
    count = 0
    sqrtn = int(n**0.5)
    for i in range(1, sqrtn+1):
        if n % i == 0:
            count += 2
    if sqrtn*sqrtn == n:
        count -= 1
    return count


n = int(input())

start = time.time()
print(divisors2(n))
end = time.time()

print(f'solve time is {end-start}')
