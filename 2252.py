# 줄세우기
# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
bigger_cnt = [0] * (N+1)
comparison = [[] for _ in range(N+1)]
queue = deque()
line = []

for _ in range(M):
    a, b = map(int, input().split())
    comparison[a].append(b)
    bigger_cnt[b] += 1

# [초기 단계] 초기 단계에서는 진입차수가 0인 모든 노드를 큐에 넣는다
for i in range(1, N+1):
    if not bigger_cnt[i]:
        queue.append(i)

#큐가 빌 때까지 다음의 과정을 반복한다 (줄을 다 세울때까지 반복)
while len(line) < N:
    now = queue.popleft()
    line.append(now)
    for p in comparison[now]:
        bigger_cnt[p] -= 1
        # 새롭게 진입차수가 0이 된 노드를 큐에 넣는다 (b)
        if not bigger_cnt[p]:
            queue.append(p)
    # 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다 (a)
    comparison[now] =[]

print(*line)

