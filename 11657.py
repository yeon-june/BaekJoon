# 벨만-포드
'''
1. 시작 정점을 결정한다.
2. 시작 정점에서 각각 다른 정점까지의 거리 값을 무한대로 초기화한다.
   (시작 정점이 a라면, distance[b] = a->b의 거리를 뜻함)
   시작 정점 -> 시작 정점은 0으로 초기화한다.
3. 현재 정점에서 모든 인접 정점들을 탐색하며, 기존에 저장되어 있는 인접 정점까지의 거리(distance[a])보다 현재 정점을 거쳐 인접 정점에 도달하는 거리가 더 짧을 경우 짧은 거리로 갱신해준다.
4. 3번의 과정을 V-1번 반복한다.
5. 위 과정을 모두 마치고 난 후 거리가 갱신되는 경우가 생긴다면 그래프에 음수 사이클이 존재한다는 것이다.
'''

# dist 갱신, 사이클 판별
def bellman_ford(start):
    dist[start] = 0
    # N번 라운드 반복 (음수 사이클 판별)
    for i in range(N):
        # 매 라운드마다 모든 간선 확인
        for j in range(M):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]
            # 경로 갱신(최단으로)
            if dist[now] != 10**10 and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost

                # 시작 정점에서 특정 정점까지 도달하기 위해 거쳐 가는 최대 간선 수는 N-1개, N번째 간선이 생기는 순간 사이클이 있다고 판단
                if i == N-1:
                    return 1
    return 0

N, M = map(int, input().split())
dist = [10**10] * (N+1)
edges = []

for _ in range(M):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

cycle = bellman_ford(1)

if cycle:
    print(-1)

else:
    for i in range(2, N + 1):
        if dist[i] == 10**10:
            print(-1)
        else:
            print(dist[i])