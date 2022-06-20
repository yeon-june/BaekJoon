# N과 M 2
# pypy3: 100ms

def dfs(s, visited, cnt):
    # 남은 숫자보다 채워야할 수가 많으면 가지치기
    if M - cnt > N - s:
        return
    
    if cnt == M:
        print(*visited)
        return

    for i in range(s+1, N+1):
        dfs(i, visited + [i], cnt+1)


N, M = map(int, input().split())
for k in range(1, N+1):
    dfs(k, [k], 1)

