# 숨바꼭질 4
# pypy3: 232
from collections import deque


def back(x):
    path = []
    tmp = x

    for _ in range(ttime[K]+1):
        path.append(tmp)
        tmp = check[tmp]

    return path[::-1]



N, K = map(int, input().split())
top = 100001
check = [-1] * top
ttime = [-1] * top

queue = deque()
queue.append(N)
check[N] = 1
ttime[N] = 0


while queue:
    now = queue.popleft()
    if now * 2 < top and check[now*2] == -1:
        queue.append(now*2)
        check[now*2] = now
        ttime[now*2] = ttime[now] + 1
       
    if 0 <= now + 1 < top and check[now + 1] == -1:
        queue.append(now+1)
        check[now+1] = now
        ttime[now+1] = ttime[now] + 1

    if 0 <= now - 1 < top and check[now-1] == -1:
        queue.append(now-1)
        check[now-1] = now
        ttime[now-1] = ttime[now] + 1


path = back(K)
print(ttime[K])
print(*path)
 
