import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for n in range(N):
    command = int(sys.stdin.readline())
    if not command:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        if command > 0:
            heapq.heappush(heap, (command, command))
        else:
            heapq.heappush(heap, (abs(command)-0.01, command))

