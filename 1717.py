# 집합의 표현
# 분리 집합 disjoint set
# pypy로 메모리 초과남
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)] # 부모 노드 초기화
# 루트 노드 찾기 & 갱신
def find(x):
    # 자기 자신이 부모면 리턴
    if x == parent[x]:
        return x
    # 부모의 부모찾기
    parent[x] = find(parent[x])
    return parent[x] 

# 합하기
def union(x,y):
    #각각 루트 찾기(어디에 속하는지)
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(M):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
