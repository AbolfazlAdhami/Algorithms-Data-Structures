def preorder(v,T):
        if v != '#':
                print(v,end=" ")
                preorder(T[v][0],T)
                preorder(T[v][1],T)
                
def inorder(v,T):
        if v != '#':
                inorder(T[v][0],T)
                print(v, end=" ")
                inorder(T[v][1], T)
                
def postorder(v,T):
        if v != '#':
                postorder(T[v][0], T)
                postorder(T[v][1], T)
                print(v, end=" ")



def solve(t):
        preorder('A',T)
        print()
        inorder('A', T)
        print()
        postorder('A', T)
        print()

N=int(input())
T={}

for _ in range(N):
        node,left,right=input().split()
        T[node]=(left,right)
solve(T)