def factorial(num):
    ans = 1
    for i in range(2,num+1):
        ans *= i

    return ans


N, K = map(int, input().split())
print(int(factorial(N)/(factorial(K)*factorial(N-K))))