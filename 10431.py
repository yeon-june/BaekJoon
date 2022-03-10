T = int(input())
for t in range(T):
    test, *students = input().split()
    cnt = 0
    for i in range(19,0,-1):
        for j in range(i):
            if int(students[j]) > int(students[j+1]):
                students[j], students[j+1] = students[j+1], students[j]
                cnt += 1

    print(f'{test} {cnt}')
