N = int(input())
M = int(input())
if M != 0:
    la = list(map(str, input()))

    N_1, N_2 = N, N

    while 1:

        if not set(map(str, str(N_1))) & set(la) and not set(map(str, str(N_2))) & set(la) and N_2 >= 0:
            k = N_1
            m = min([len(str(N_1)),len(str(N_2))])
            break
        elif not set(map(str, str(N_1))) & set(la):
            k = N_1
            m = len(str(N_1))
            break
        elif not set(map(str, str(N_2))) & set(la):
            if N_2 >= 0:
                k = N_2
                m = len(str(N_2))
                break

        if N_1 == 100 or N_2 == 100:
            k = 100
            m = 3
            break

        N_1 += 1
        N_2 -= 1


    print(min(abs(N-k) + m, abs(N-100)))

else:
    print(min([len(str(N)), abs(100-N)]))