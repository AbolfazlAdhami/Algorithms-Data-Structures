# def factorize(n):
#         if n<2:
#                 return []
#         else:
#                 for i in range(2,int(n**0.5)+1):
#                         if n%i==0:
#                                 return [i]+factorize(n//i)
#                 return [n]

# def factorize(n, m):
#     if n < 2:
#         return []
#     elif m > int(n**0.5):
#         return [n]
#     elif n % m == 0:
#         return [m]+factorize(n//m, m)
#     else:
#         return factorize(n, m+1)


def factorize(n):
        factors=[]
        for i in range(2,int(n**0.5)+1):
                while n%i==0:
                        factors.append(i)
                        n//=i
        if n!=1:
                factors.append(n)
        return factors



def solve():
    N = int(input())
    factors = factorize(N)
    print(" ".join(map(str, factors)))


solve()
