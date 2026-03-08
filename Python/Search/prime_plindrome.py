def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)


# def solve(n, m):
#     count = 0
#     s = []
#     for i in range(n, m+1):
#         if is_prime(i) and is_palindrome(i) :
#             count += 1
#             s.append(i)
#     return (count, s)


def solve(n, m):
    count = 0
    s = []
    for i in range(n, m+1):
        if is_palindrome(i) and is_prime(i):
            count += 1
            s.append(i)
    return (count, s)


N, M = map(int, input().split())
print(solve(N, M))
