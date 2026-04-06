F = [0, 1]


def fib(n):
        if n < len(F):
               return F[n]
        else:
                for _ in range(len(F), n+1):
                       F.append(F[-1]+F[-2]%1007)
                return F[n]


def print_fib(n, arr):
       for i in range(n):
               print(f'F[{arr[i]}] = {fib(arr[i])}')

N = int(input())
A=[int(input()) for _ in range(N)]
print_fib(N, A)
