from heapq import heappop, heappush


def min_heap(cmd,heap):
        if cmd[0] == 'push':
                heappush(heap,int(cmd[1]))
        elif cmd[0] == 'pop':
                print(0 if not heap else heappop(heap))
        print(cmd,heap)
   
        
def max_heap(cmd,heap):
        if cmd[0] == 'push':
                heappush(heap,-int(cmd[1]))
        elif cmd[0] == 'pop':
                print(0 if not heap else -heappop(heap))
        print(cmd,heap)
       
       
        
N= int(input())
heap=[]
for _ in range(N):
        cmd=input().split()
        max_heap(cmd,heap)
        
