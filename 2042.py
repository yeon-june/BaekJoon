# 세그먼트 트리
# 현재 노드는 왼쪽, 오른쪽 자식 노드 값을 더한 값

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] * N
# 세그먼트 트리를 만들 수 있는 기틀, 
# 배열(arr)의 개수가 N개일 때, N보다 큰 가장 가까운 N의 제곱수를 구한 뒤에 그것의 2배를 하여 미리 세그먼트 트리의 크기를 만들어놓어야 한다
# 실제로는 데이터의 개수 N에 4를 곱한 크기만큼 미리 세그먼트 트리의 크기를 할당한다
segment_tree = [0] * (N*4) 

# 트리 만들기
# start~end : 트리 노드 범위, index: 시작 노드
def init(start, end, index):
    # 리프 노드, arr의 값 그대로
    if start == end:
        segment_tree[index] = arr[start-1]
        return segment_tree[index]
    
    # 왼쪽, 오른쪽 자식 노드 더하기
    mid = (start+end)//2
    segment_tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2 + 1)
    return segment_tree[index]

# 값 찾기
# start, end : 트리의 시작과 끝
# left, right: 더할 범위
def find(start, end, index, left, right):
    # 범위 넘어갈 때
    if start > right or end < left:
        return 0

    # 현재 상태로 구할 수 있을 때
    if left <= start and end <= right:
        return segment_tree[index]

    mid = (start+end) // 2
    # 왼노드 + 오른노드
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sub_sum

# 트리 값 바꾸기 (업데이트)
# update_data 는 원래 값과의 차이 (바뀔 값 - 현재 값)
# start, end, 노드 범위, index => 현재 업데이트할,,
# update_idx => 업데이트 되는 idx
def update(start, end, index, update_idx, update_data):
    # 업데이트 불가 범위
    if start > update_idx or end < update_idx:
        return 
    
    segment_tree[index] += update_data

    if start == end:
        return
    
    mid = (start + end)//2
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)

for i in range(N):
    arr[i] = int(input())

# idx * 2 && idx *2 + 1로 좌 우 노드를 편하게 계산하기 위해 start idx 1로 시작 
init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a==1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, N, 1, b, diff)
    
    else:
        print(find(1, N, 1, b, c))