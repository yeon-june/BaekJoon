'''
python3: 5984ms
'''

from itertools import combinations
import sys
sys.setrecursionlimit(10**6)


N = int(input())
synergy = []
for n in range(N):
    synergy.append(list(map(int, input().split())))
all_p = set(range(N))
teams = list(map(set, combinations(all_p, N//2)))


def get_synergy(lst):
    two = combinations(lst,2)
    syn = 0
    for t in two:
        a, b = t[0], t[1]
        syn += synergy[a][b]
        syn += synergy[b][a]
    
    return syn


min_dif = 10**10
def balance(teams):
    global min_dif

    if not teams:
        return
    
    t1 = teams[-1]
    t2 = all_p - t1
    teams.pop()
    teams.remove(t2)
    synergy1 = get_synergy(t1)
    synergy2 = get_synergy(t2)

    if abs(synergy1 -synergy2) < min_dif:
        min_dif = abs(synergy1 -synergy2)

    balance(teams)

balance(teams)

print(min_dif)
