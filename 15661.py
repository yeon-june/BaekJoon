'''
heap & 
pypy3: 3728ms
'''

N = int(input())
synergy = [list(map(int,input().split())) for _ in range(N)]
visited = [0] * N

min_dif = 10**10

def recur(num):

    if num == N:
        get_syn()
        return

    visited[num] = 1
    recur(num+1)
    visited[num] = 0
    recur(num+1)
            
    

def get_syn():
    global min_dif

    start = 0
    link = 0

    for i in range(N-1):
        for j in range(i+1,N):
            if visited[i] and visited[j] :
                start += synergy[i][j] + synergy[j][i]
            elif not visited[i] and not visited[j]:
                link += synergy[i][j] + synergy[j][i]
    
    diff = abs(start-link)

    if  min_dif > diff:
        min_dif = diff



recur(0)
print(min_dif)