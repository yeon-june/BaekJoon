from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([0]*2*N)

turn = 1
while 1:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
	belt.rotate(1)
	robots.rotate(1)
	robots[N-1] = 0
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
	for i in range(N-2,-1,-1):
		if robots[i] and not robots[i+1] and belt[i+1]:
			belt[i+1]-=1
			robots[i+1], robots[i] = robots[i], 0

    #N번째 로봇 내리기
	robots[N-1]=0
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
	if not robots[0] and belt[0]:
		robots[0] = 1
		belt[0] -= 1
	if belt.count(0) >= K:
		print(turn)
		break
	turn += 1