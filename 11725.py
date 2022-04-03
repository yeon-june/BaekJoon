'''
pypy3: 428ms
'''

from collections import defaultdict, deque
connected = defaultdict(list)

N = int(input())
for n in range(N-1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

parent = [0] * (N+1)
root = 1
queue = deque()
queue.append(root)
parent[root] = -1

while queue:
    node = queue.popleft()
    for child in connected[node]:
        if not parent[child]:
            parent[child] = node
            queue.append(child)

for i in range(2, N+1):
    print(parent[i])



