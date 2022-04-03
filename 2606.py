'''
pypy3: 140ms
python3: 112ms
'''

from collections import defaultdict, deque

N = int(input())
K = int(input())
net = defaultdict(list)
for k in range(K):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

infected = [1]
connected = deque()
connected.extend(net[1])
infected.extend(net[1])

while connected:
    now = connected.popleft()
    for com in net[now]:
        if com not in infected:
            connected.append(com)
            infected.append(com)

print(len(infected)-1)
