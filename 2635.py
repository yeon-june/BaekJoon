def max_num_lst(initial):
    # 최대 길이 l
    l = 0
    # 주어진 값보다 작은 값에서 for~
    for i in range(initial,0, -1):
        # 초기 리스트
        n_lst = [initial, i]
        # while 내에서 변수
        k = 0
        while 1:
            # 다음 수 구하기
            n = n_lst[k] - n_lst[k+1]
            # 0보다 작을 때 break
            if n < 0:
                # 최대 길이 판단
                if l < len(n_lst):
                    l = len(n_lst)
                    max_list = n_lst
                break
            # 리스트에 n 추가
            n_lst.append(n)
            # k 증가
            k += 1

    # 반환 값
    return print(l), print(*max_list)




N = int(input())
max_num_lst(N)

    
