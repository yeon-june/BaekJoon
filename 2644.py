import sys
input = sys.stdin.readline

def dfs(now, cnt):
    re_cnt[now] = cnt
    if now == B:
        return

    for per in relation[now]:
        if re_cnt[per] == -1:
            dfs(per, cnt+1)


N = int(input())
A, B = map(int, input().split())

M = int(input())
relation = [[] for _ in range(N+1)]
re_cnt = [-1]*(N+1)

for _ in range(M):
    p, c = map(int, input().split())
    relation[p].append(c)
    relation[c].append(p)

dfs(A, 0)
print(re_cnt[B])