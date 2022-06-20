N, K = map(int, input().split())
nations = [0] * (N+1)
for _ in range(N):
    nat, G, S, C = map(int, input().split())
    nations[nat] = (G, S, C)

comp = nations[K]
rank = 1
for j in range(1, N+1):
    now = nations[j]
    if now[0] > comp[0]:
        rank += 1
    elif now[0] == comp[0] and now[1] > comp[1]:
        rank += 1
    elif now[0] == comp[0] and now[1] == comp[1] and now[2]> comp[2]:
        rank += 1

print(rank)