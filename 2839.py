# 설탕배달 DP
# 사탕가게에 설탕을 정확하게 N킬로그램을 배달
# 최대한 적은 봉지, 3킬로그램 봉지와 5킬로그램 봉지
N = int(input())
sugar = [10**10] *(N+1)
sugar[3] = 1
if N >=5:
    sugar[5] = 1

for i in range(6, N+1):
    sugar[i] = min(sugar[i-3]+1, sugar[i-5]+1, 10**10)

if sugar[N] == 10**10:
    print(-1)
else:
    print(sugar[N])