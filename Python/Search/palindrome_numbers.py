# def is_palindrome(n):
#     r, m = 0, n
#     while m > 0:
#         r *= 10
#         r += m % 10
#         m //= 10
#     return n == r


def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return int(s) == int(r)


def solve(n, m):
    count = 0
    for i in range(n, m+1):
        if is_palindrome(i):
            count += 1
    return count


N, M = map(int, input().split())
print(solve(N, M))
