import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())

G1 = list(reversed(list(input().rstrip())))
G2 = list(input().rstrip())

T = int(input())

line = G1[:] + G2[:]
time = 0
while time < T:
    new_line = line[:]
    i=0
    while i < len(line)-1:
        if line[i] in G1 and line[i+1] in G2:
            new_line[i] , new_line[i+1] = new_line[i+1], new_line[i]
            i += 2 
        else:
            i += 1
    line = new_line[:]
    time += 1   

print(''.join(line))        