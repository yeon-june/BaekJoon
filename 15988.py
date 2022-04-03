'''
미리 경우 다 정해놓고 뽑아내기
python3: 564ms
'''

lst = [0, 1, 2, 4]
for i in range(4, 1000001):
    lst.append((lst[i-1] + lst[i-2] + lst[i-3]) % 1000000009)

T = int(input())
for t in range(T):
    N = int(input())
    ans = lst[N]
    print(ans)