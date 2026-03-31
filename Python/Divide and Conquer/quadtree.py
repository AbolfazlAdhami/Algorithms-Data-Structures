def quadtree(i,j,n,A):
        chk =check(i,j,n,A)
        
        if chk < 2:
                return 'W' if chk == 0 else 'B'
        else:
                n//=2
                return 'Q'+quadtree(i,j,n,A)+quadtree(i,j+n,n,A)+quadtree(i+n,j,n,A)+quadtree(i+n,j+n,n,A)
        
def check(i,j,n,A):
        for x in range(i,i+n):
                for y in range(j,j+n):
                        if A[i][j] != A[x][y]:
                                return 2
        return A[i][j]  
        
        
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
print(quadtree(0,0,N,A))