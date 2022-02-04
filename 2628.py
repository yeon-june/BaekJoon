#가로, 세로 받기
width, height = map(int, input().split())

#자르는 횟수
N = int(input())
#가로, 세로 자르는 부분
cut_dict = {0: [0, height], 1: [0, width]}
for n in range(N):
    w_h, num = map(int, input().split())
    cut_dict[w_h].append(num)



height_cut = cut_dict[0]
width_cut= cut_dict[1]
width_cut.sort()
height_cut.sort()

#가로, 세로 길이들 저장
width_len = []
height_len = []
for i in range(len(width_cut)-1):
    width_len.append(width_cut[i+1] - width_cut[i])
for j in range(len(height_cut)-1):
    height_len.append(height_cut[j+1] - height_cut[j])

#최대 * 최대
print(max(width_len) * max(height_len))
