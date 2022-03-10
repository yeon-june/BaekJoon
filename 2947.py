seq = list(map(int, input().split()))
process = []
N = 5
for i in range(N-1, 0, -1):
    for j in range(i):
        if seq[j] > seq[j+1]:
            seq[j], seq[j+1] = seq[j+1], seq[j]
            print(*seq)
        if seq == [1, 2, 3, 4, 5]:
            exit()
