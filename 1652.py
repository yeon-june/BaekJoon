def lying_down(R):
    tot = 0
    for row in R:
        cnt = 0
        for j in range(N):
            if row[j] == '.':
                cnt += 1
                if j == N-1 and cnt >= 2:
                    tot += 1
            else:
                if cnt >= 2:
                    tot += 1
                cnt = 0

    return tot


N = int(input())
room = [list(input()) for _ in range(N)]
room90 = list(map(list, zip(*reversed(room))))

vertical = lying_down(room90)
horizontal = lying_down(room)

print(horizontal, vertical)