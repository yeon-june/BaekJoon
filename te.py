from collections import deque
import sys

def dfs(i):
    global correct, dpt
    # print('초기점 : ',p)
    # print('깊이 : ',dpt)
    # print(visited)
    for k in range(len(adj[i])):
        if visited[adj[i][k]] == 0:
            visited[adj[i][k]] = 1
            dpt += 1
            dfs(adj[i][k])

        # 다시 초기점으로 돌아왔을 때,
        # 홀수각형 사이클이면 이분 불가능
        elif adj[i][k] == p and dpt > 2:
            if dpt%2 == 1:
                correct = 1
            return

    else:        
        dpt -= 1
        visited[i] = 0
        return


K = int(input())
for _ in range(K):
    N, M = map(int, sys.stdin.readline().split())
    adj = deque()
    for _ in range(N+1):
        adj.append([])
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    correct = 0
    ans = 'YES'
    for p in range(N+1):
        visited = [0] * (N+1)
        if sum(adj[p]) != 0 and visited[p] == 0:
            visited[p] = 1
            dpt = 1
            dfs(p)
            if correct == 1:
                ans = 'NO'
                break
    
    print(ans)