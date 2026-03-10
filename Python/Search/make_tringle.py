# def solve(n):
#         cnt=0
#         for a in range(1,n):
#                 for b in range(a,n):
#                         for c in range(b,n):
#                                 if a+b+c==n and a+b>c:
#                                         cnt+=1
#         return cnt

# def solve(n):
#         cnt=0
#         for a in range(1,n):
#                 for b in range(a,n):
#                         c=n-a-b
#                         if b<=c and a+b >c:
#                                 cnt+=1
#         return cnt
# def solve(n):
#         cnt=0
#         for c in range((n+1)//3,(n+1)//2):
#                 for b in range((n-c+1)//2,c+1):
#                         cnt+=1
                
#         return cnt
def solve(n):
        cnt=0
        for c in range((n+1)//3,(n+1)//2):
                cnt+= c-(n-c+1)//2+1
                
        return cnt


n=int(input())
print(solve(n))