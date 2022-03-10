def movement(piece, move):
    piece_tmp = piece[::]
    
    if move == 'R':
        if piece_tmp[1] + 1 in range(1, 9):
            piece_tmp[1] += 1
    elif move == 'L':
        if piece_tmp[1] - 1 in range(1, 9):
            piece_tmp[1] -= 1
    elif move == 'B':
        if piece_tmp[0] - 1 in range(1, 9):
            piece_tmp[0] -= 1
    elif move == 'T':
        if piece_tmp[0] + 1 in range(1, 9):
            piece_tmp[0] += 1
    elif move == 'RT':
        if piece_tmp[0] + 1 in range(1, 9) and piece_tmp[1] + 1 in range(1,9):
            piece_tmp[0] += 1
            piece_tmp[1] += 1
    elif move == 'LT':
        if piece_tmp[0] + 1 in range(1, 9) and piece_tmp[1] - 1 in range(1,9):
            piece_tmp[0] += 1
            piece_tmp[1] -= 1
    elif move == 'RB':
        if piece_tmp[0] - 1 in range(1, 9) and piece_tmp[1] + 1 in range(1,9):
            piece_tmp[0] -= 1
            piece_tmp[1] += 1
    elif move == 'LB':
        if piece_tmp[0] - 1 in range(1, 9) and piece_tmp[1] - 1 in range(1,9):
            piece_tmp[0] -= 1
            piece_tmp[1] -= 1
    
    return piece_tmp



col_dict = {'A':1 , 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

king, stone, N = input().split()
N = int(N)
#행, 열 tuple로 좌표 지정
king = [int(king[1]), col_dict[king[0]]]
stone = [int(stone[1]), col_dict[stone[0]]]
moves = []
for n in range(N):
    moves.append(input())

for move in moves:
    king_tmp = movement(king, move)
    if king_tmp == king:
        pass
    else:
        if king_tmp == stone:
            stone_tmp = movement(stone, move)
        
            if stone_tmp == stone:
                pass
            else:
                king = king_tmp
                stone = stone_tmp
        else:
            king = king_tmp

print(''.join([col_dict[king[1]], str(king[0])]))
print(''.join([col_dict[stone[1]], str(stone[0])]))

