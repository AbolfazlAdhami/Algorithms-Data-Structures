def quadtree(i,j,n,s,T):
        head=get_next(s)
        
        if head == 'W' or head == 'B':
                for x in range(i,i+n):
                        for y in range(j,j+n):
                                T[x][y]= 0 if head == 'W' else 1
        else:
                n//=2
                quadtree(i,j,n,s,T)
                quadtree(i,j+n,n,s,T)
                quadtree(i+n,j,n,s,T)
                quadtree(i+n,j+n,n,s,T)
        
        
        
        
idx=-1
def get_next(s):
        global idx
        idx+=1
        return s[idx]


def solve(n,s):
        T=[[0]* n for _ in range(n)]
        quadtree(0,0,n,s,T)
        
        for i in range(n):
                print(*T[i])
                
                
N=int(input())
s=input().upper()
solve(N,s)