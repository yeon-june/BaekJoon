def calcYear(E, S, M):
    # 세 숫자가 같으면 바로 출력
    if E == S == M:
        return E
    else:
        # E가 범위가 가장 작기 때문에 기준점 (15가 몇번이나 돌아갔을까?)
        n = 1
        while 1:
            rE = 15 * n + E
            # 다음 작은 범위의 M(E보다 작은 사이클)
            for j in range(n):
                rM = 19 * j + M
                # S가 가장 마지막(M이랑 같을 수 있음)
                for i in range(j+1):
                    rS = 28 * i + S
                    if rE == rS == rM:
                        return rE
                    else:
                        pass
            n += 1



E, S, M = map(int, input().split())
print(calcYear(E, S, M))

