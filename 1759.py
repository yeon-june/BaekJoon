'''
pypy3: 116ms
'''

from itertools import combinations

vowel = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
letters = list(input().split())
Vo = []
Co = []
for le in letters:
    if le in vowel:
        Vo.append(le)
    else:
        Co.append(le)


result = []
for i in range(1, L-1):
    j = L - i
    v_combi = list(map(list, combinations(Vo, i)))
    c_combi = list(map(list, combinations(Co, j)))
    for vs in v_combi:
        for cs in c_combi:
            tmp = []
            tmp += vs
            tmp += cs
            tmp.sort()
            result.append(''.join(tmp))


result.sort()
for r in result:
    print(r)