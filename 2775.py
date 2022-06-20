# 부녀회장이될테야
# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
# 해당 집에 거주민 수를 출력

T = int(input())
for t in range(T):
    K = int(input())
    N = int(input())
    apartment = [[0]*(N+1) for _ in range(K+1)]
    apartment[0] = [i for i in range(N+1)]

    for k in range(1,K+1):
        for n in range(1,N+1):
            if n == 1:
                apartment[k][n] = apartment[k-1][n]
            else:
                apartment[k][n] = apartment[k][n-1] + apartment[k-1][n]
        
    
    print(apartment[K][N])