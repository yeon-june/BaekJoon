import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for n in range(N):
    command = int(sys.stdin.readline())
    if command:
        heapq.heappush(heap, command)
    
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)