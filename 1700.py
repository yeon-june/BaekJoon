# 어딜 기준으로 잡을지
# i 번째 왔을 때 뭘 뺄지 고르자
def unplugging(i, K):
    for k in range(K+1):
        if plugged[k] and k not in seq[i+1:]:
            plugged[k] = 0
            return

    else:
        for j in range(K-1, i, -1):
            if plugged[seq[j]] and seq[j] not in seq[i+1: j]:
                plugged[seq[j]] = 0
                return


N, K = map(int, input().split())
seq = list(map(int, input().split()))
plugged = [0] * (K+1)

cnt = 0
for j in range(K):
    if sum(plugged) < N:
        plugged[seq[j]] = 1
    elif plugged[seq[j]]:
        pass
    elif not plugged[seq[j]]:
        cnt += 1
        unplugging(j, K)
        plugged[seq[j]] = 1

print(cnt)


