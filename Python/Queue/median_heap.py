from heapq import heappop, heappush


def solve(N):
        maxheap,minheap=[],[]
        
        for n in N:
                heappush(maxheap,-n)
                heappush(minheap,-heappop(maxheap))
                if len(maxheap) < len(minheap):
                        heappush(maxheap,-heappop(minheap))
                print(-maxheap[0],end=" ")
                
        print(maxheap,minheap)
        
N=list(map(int,input().split()))
solve(N)