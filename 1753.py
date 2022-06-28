# 최단 경로 (다익스트라 - heapq 사용)

import heapq

def dijkstara(start):
    dist[start] = 0
    heapq.heappush(heap,(0, start)) # (시작으로부터 거리, 노드)

    # 최소 힙이 남아 있을 동안
    while heap:
        weight, now = heapq.heappop(heap)

        # 현재의 가중치가 더 작을 경우 무시(now를 경유할 필요가 없을 경우)
        if dist[now] < weight: #현재까지의 최소 거리,  +a해야하는 지금 확인 할 경로 
            continue 
        
        # 경유 할 필요가 있는지 확인
        for next_node, w in arr[now]:
            next_weight = w + weight # now~next + now 까지의 거리

            # 경유 시 더 짧은 거리 rodtls
            if next_weight < dist[next_node]:
                dist[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))


heap = [] # 최소 힙
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
dist = [10**10] * (V+1)
K = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v,w))

dijkstara(K)
for n in range(1, V+1):
    print('INF' if dist[n] == 10**10 else dist[n])