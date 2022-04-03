import sys
import heapq

N = int(sys.stdin.readline()) # sys 안쓰면 시간 초과 뜸
heap = []
for n in range(N):
    command = int(sys.stdin.readline())
    if command:
        heapq.heappush(heap, (-command, command))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)