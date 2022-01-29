N = int(input())

for i in range(100):
    if N == 1:
        print(1)
        break
    elif 1 + (i-1)*(6+6*(i-1))/2 < N <=  1 + (i)*(6+6*(i))/2:
        print(i+1)
        break