from collections import defaultdict

def continuous(nubmers):
    start = 0
    for i in range(10):
        if numbers[i] == 1:
            start = i
            break
    if not start:
        return 0
    else: 
        for j in range(5):
            if numbers[start+j] != 1:
                return 0
    
    return 1


cards = defaultdict(list)
numbers = [0] * 10
nums = []
R = 0
B = 0
Y = 0
G = 0
for _ in range(5):
    C, N = input().split()
    cards[C].append(int(N))
    if C == 'R':
        R += 1
    elif C == 'B':
        B += 1
    elif C == 'Y':
        Y += 1
    else:
        G += 1
    
    numbers[int(N)] += 1
    nums.append(int(N))


if 5 in [R, B, Y, G]:
    # 1. 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 점수는 가장 높은 숫자에 900을 더한다. 
    if continuous(numbers):
        print(max(nums) + 900)
    
    # 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다
    else:
        print(max(nums) + 600)

# 카드 5장 중 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다
elif 4 in numbers:
    for i in range(10):
        if numbers[i] == 4:
            print(i+800)
            break

# 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다        
elif 3 in numbers and 2 in numbers:
    result = 700
    for i in range(10):
        if numbers[i] == 3:
            result += i*10
        elif numbers[i] == 2:
            result += i
    print(result)

# 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다
elif continuous(numbers):
    print(max(nums) + 500)

# 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
elif 3 in numbers:
    for i in range(10):
        if numbers[i] == 3:
            print(i + 400)
            break

# 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
elif numbers.count(2) == 2:
    sames = []
    for i in range(10):
        if numbers[i] == 2:
            sames.append(i)

    print(300 + max(sames)*10 + min(sames))

# 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다
elif 2 in numbers:
    for i in range(10):
        if numbers[i] == 2:
            print(i+200)
            break

else:
    print(max(nums) + 100)
        