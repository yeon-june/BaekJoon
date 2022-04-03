# ABCDE
# pypy3: 756ms

from collections import defaultdict


def find_friends(start):
    def dfs(start, pre, cnt):
        global ans

        if cnt == 4:
            ans = 1
            return

        for next in graph[start]:
            if next not in pre:
                dfs(next, pre + [next], cnt + 1)
    
    dfs(start, [start], 0)


N, M = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

ans = 0
for i in range(N):
    find_friends(i)
    if ans:
        break

print(ans)

