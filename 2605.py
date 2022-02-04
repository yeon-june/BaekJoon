N = int(input())
# 뽑은 수 리스트
num = list(map(int, input().split()))
# 초기 값
line = [n+1 for n in range(N)]

# 규칙대로 앞으로 가기, 그대로 있기
for i in range(N):
    if num[i] != 0:
        line.insert(i - num[i], line[i])
        del line[i+1]

print(*line)