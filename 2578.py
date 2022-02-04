#대각선 저장
def diagnal(N,array):
    d =[]
    for i in range(N):
       d.append(array[i][i])
    return d

def diagnal_rev(N,array):
    d =[]
    for i in range(N):
        d.append(array[i][N-i-1])
    return d

# 빙고 진행
# bingo_board: 각 행, 열, 대각선 딕셔너리
# call했을 때 행 열 별로 지워진 숫자 수 딕셔너리
# call 숫자 리스트
def bingo_call(bingo_board, check_board, call):
    N = 0
    for num in call:
        N += 1
        for key in bingo_board.keys():
            for i in range(5):
                #
                if num == bingo_board[key][i]:
                    check_board[key] += 1
            # 빙고 3줄 일때 멈추기
            if list(check_board.values()).count(5) == 3:
                return N


# 빙고보드 만들기
bingo_row =[]
for i in range(5):
    bingo_row.append(list(map(int, input().split())))

call = []
for i in range(5):
    call.extend(list(map(int,input().split())))

bingo_column = list(map(list,zip(*bingo_row)))
bingo_board = dict()
for n in range(5):
    bingo_board[n] = bingo_row[n]
    bingo_board[n+5] = bingo_column[n]
bingo_board['d1'] = diagnal(5,bingo_row)
bingo_board['d2'] = diagnal_rev(5,bingo_row)

check_board = dict()
for key in bingo_board.keys():
    check_board[key] =0

print(bingo_call(bingo_board, check_board, call))



