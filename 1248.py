import pprint

N = int(input())
info = list(input())

info_arr = [[0]*(N+1), [0]+info[:N]]
start = N
add = N-1
while start < len(info):
    info_arr.append([0]*(N-add+1) + info[start:start+N-1])
    start += add
    add -= 1
pprint.pprint(info_arr)
minus_used = [0] * 11
plus_used = [0] * 11


def search_nums(cnt, result, minus_used, plus_used):
    if cnt == N+1:
        if check(result):
            print(*result)
            exit()
        return
    
    if info_arr[cnt][cnt] == '0':
        result[cnt-1] = 0
        search_nums(cnt+1, result, minus_used, plus_used)
    else:
        for h in range(1,10):
            if info_arr[cnt][cnt] == '+':
                if not plus_used[h]:
                    result[cnt-1] = h
                    plus_used[h] = 1
                    search_nums(cnt+1, result, minus_used, plus_used)
                    result[cnt-1] = 0
                    plus_used[h] = 0
            elif info_arr[cnt][cnt] == '-':
                if not minus_used[h]:
                    result[cnt-1] = -1 * h
                    minus_used[h] = 1
                    search_nums(cnt+1, result, minus_used, plus_used)
                    result[cnt-1] = 0
                    minus_used[h] = 0



def check(lst):
    for i in range(1,N):
        for j in range(i+1,N):
            ssum = sum(lst[i-1:j])
            if ssum > 0 and info_arr[i][j] == '+':
                pass
            elif ssum == 0 and info_arr[i][j] == '0':
                pass
            elif ssum < 0 and info_arr[i][j] == '-':
                pass
            else:
                return False
    return True


search_nums(1, [0]*N, minus_used, plus_used)