'''
import sys      
sys.setrecursionlimit(10**6)


def dfs(now, visited, cnt):
    global min_trial
    
    if now == K:
        if cnt < min_trial:
            min_trial = cnt
            return
    
    if cnt >= min_trial:
        return

    if now > K:
        new_lst = [now-1]
    
    else:
        new_lst = [now+1, 2*now]

    for new in new_lst:
        if new >= 0 and new not in visited:
            visited.append(new)
            dfs(new, visited, cnt + 1)
            visited.pop()


N, K = map(int, input().split())
visited = [N]

min_trial = 10**10
dfs(N, visited, 0)
print(min_trial)
'''

'''
pypy3: 156ms
'''
from collections import deque


def bfs(start, visited):
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        if now == K:
            print(visited[now])
            break

        new_lst = [now-1, now+1, 2*now]

        for new in new_lst:
            if new >= (10**5 + 100) or new < 0:
                continue
            else:
                if not visited[new] and new != start:
                    visited[new] = visited[now] + 1
                    queue.append(new)



N, K = map(int, input().split())
visited = [0] * (10**5 + 100)

bfs(N, visited)