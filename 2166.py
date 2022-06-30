# https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84
# 면적 = 1/2 x 둘레길이 x 변심거리. 
# 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다

import sys
input = sys.stdin.readline

N = int(input())
ans = 0
x, y = [], []

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x += [x[0]]
y += [y[0]]

for i in range(N):
    ans += (x[i]*y[i+1] - x[i+1]*y[i])

print(round(abs(ans)/2,1))