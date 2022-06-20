# N과 M 4
# pypy3: 240ms

def dfs(s, visited, cnt):    
    if cnt == M:
        print(*visited)
        return

    for i in range(s, N+1):
        dfs(i, visited + [i], cnt+1)


N, M = map(int, input().split())
for k in range(1, N+1):
    dfs(k, [k], 1)

