N = int(input())
channels = []
for i in range(N):
    channel = input()
    if channel == 'KBS1':
        ch1 = i
    elif channel == 'KBS2':
        ch2 = i

    channels.append(channel)

result = ''
# KBS1까지 이동
result += '1'* ch1
# KBS1 첫번째로 변경
result += '4' * ch1
# KBS1 옮기는 과정에서 KBS2 변화
if ch1 > ch2:
    ch2 += 1

result += '1' * ch2
result += '4' * (ch2-1)

print(result)