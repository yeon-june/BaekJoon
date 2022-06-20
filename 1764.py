N, M = map(int, input().split())

not_heard = set()
for _ in range(N):
    not_heard.add(input())
not_seen = set()
for _ in range(M):
    not_seen.add(input())

not_heardseen = not_heard&not_seen
not_heardseen = list(not_heardseen)
not_heardseen.sort()
print(len(not_heardseen))
for name in not_heardseen:
    print(name)