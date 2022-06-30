def is_valid(now, nxt):
    r = abs(now[0] - nxt[0])
    c = abs(now[1] - nxt[1])
    if ((r,c) in [(2,1),(1,2)]) and (nxt not in visited):
        return 1
    return 0

moves = [0] * 36
visited = []
ans = 'Valid'
for i in range(36):
    moves[i] = list(input())
    moves[i][0] = ord(moves[i][0])
    moves[i][1] = int(moves[i][1])
visited.append(moves[0])
for j in range(35):
    now = moves[j]
    nxt = moves[j+1]
    if not is_valid(now,nxt):
        ans = 'Invalid'
        break
    visited.append(nxt)

lr = abs(moves[-1][0] - moves[0][0])
lc = abs(moves[-1][1] - moves[0][1])

if (lr,lc) not in [(2,1),(1,2)]:
    ans = 'Invalid'

print(ans)