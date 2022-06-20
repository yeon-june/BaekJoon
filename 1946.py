# 정렬

T = int(input())
for t in range(T):
    N = int(input())
    appliants = []
    for i in range(N):
        a, b = map(int, input().split())
        appliants.append([a,b])

    appliants.sort() # 앞사람들은 이미 서류는 뒷사람들보다 높음
    cur_mx = appliants[0][1]
    employing = 1

    for i in range(1, N):
        if cur_mx > appliants[i][1]:
            employing += 1
            cur_mx = appliants[i][1]

    print(employing)