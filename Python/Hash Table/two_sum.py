def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return num_map


# def solve(n, k, s):
#     for i in range(n):
#         for j in range(i+1, n):
#             if s[i] + s[j] == k:
#                 return (i, j)
#             elif j == n:
#                 return -1


def solve(n,k,s):
    for i in range(n):
        if k -s[i] in s and i < s.index(k-s[i]):
            return(s[i],k-s[i])
        
        
def solve_pro(n,k,s):
    d = {s[i]:k-s[i] for i in range(n)}
    
    for i in range(n):
        if d[s[i]] in d and i < s.index(d[s[i]]):
            print(s[i],k-s[i])

N, M = map(int, input().split())
S = list(map(int, input().split()))
solve_pro(N, M, S)
