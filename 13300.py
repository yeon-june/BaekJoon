# 학생 수 저장
student_dict = {0: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}, 
                1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0} }

# 전체 명수, 최대 인수
N, K = map(int, input().split())

# 학생 수 기록
for n in range(N):
    S, C = map(int, input().split())
    if S == 0:
        student_dict[0][C] += 1
    else:
        student_dict[1][C] += 1

# 규칙에 필요한 방 수 더하기
room = 0
for j in range(2):
    for i in range(1, 7):
        if student_dict[j][i] % K:
            room += student_dict[j][i]//K + 1
        else:
            room += student_dict[j][i]//K
print(room)
