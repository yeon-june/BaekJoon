from collections import deque
top = 100001
check = [0] * top
ttime = [-1] * top

N, K = map(int, input().split())
queue = deque()
queue.append(N)
check[N] = 1
ttime[N] = 0

while queue:
    now = queue.popleft()
    # 순간 이동 -> 우선순위 1
    if now*2 < top and not check[now*2]:
        queue.appendleft(now*2)
        check[now*2] = 1
        ttime[now*2] = ttime[now]
    
    # x+1 이동
    if now + 1 < top and not check[now+1]:
        queue.append(now+1)
        check[now+1] = 1
        ttime[now+1] = ttime[now] + 1

    # x-1 이동
    if now - 1 >= 0 and not check[now-1]:
        queue.append(now-1)
        check[now-1] = 1
        ttime[now-1] = ttime[now] + 1
        
print(ttime[K])