from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque(False for _ in range(N))

depth = 0
zeroCount = 0
while True:
    if zeroCount >= K:
        print(depth)
        break

    # 1. 컨베이어 벨트와 로봇을 1칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)

    # 로봇이 내리는 위치는 바로 내리도록 한다.
    robot[N - 1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 한 칸씩 옆으로 이동하게 한다.
    # (N-2, N-1) ~ (-1, 0) 까지 밀어준다. # 테트리스와 비슷
    for i in range(N - 2, -1, -1):
        if robot[i]:
            # 다음 칸 내구도 & 로봇 유무 판단
            if belt[i+1] >= 1 and not robot[i+1]:
                robot[i+1], robot[i] = True, False
                belt[i+1] -= 1
                if not belt[i+1]:
                    zeroCount += 1


    # 옆으로 이동했으므로, 내리는 위치는 다시 판단해준다.
    robot[N - 1] = False

    # 3. 올리는 칸에 로봇을 올린다.
    if belt[0]:
        robot[0] = True
        belt[0] -= 1
        if not belt[0]:
            zeroCount += 1

    depth += 1