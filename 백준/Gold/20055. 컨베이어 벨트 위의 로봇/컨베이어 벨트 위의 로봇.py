from collections import deque

N, K = map(int, input().split())
remain = list(map(int, input().split()))
judge = [False for _ in range(2*N)]

upCursor = 0 # 올리는 위치
downCursor = N-1 # 내리는 위치

depth = 0 # 단계
zeroCount = 0 # 내구도가 0인 칸의 개수
robot = deque() 

while True:
    if zeroCount >= K:
        break
    # 1바퀴 회전
    upCursor -= 1
    downCursor -= 1

    if upCursor == -2*N:
        upCursor = 0
        downCursor = N-1

    # 1. 이전에 배치된 로봇들이 이동 가능한 지 파악
    for _ in range(len(robot)):
        r = robot.popleft()
        judge[r] = False # 이동하기 위해, 일단 현재 위치 로봇 제거

        # 내리는 위치일 경우
        if r == downCursor or r == downCursor - (2*N):
            continue

        # 내리는 위치가 아닐 경우
        else:
            if not judge[r+1] and remain[r+1]: # 다음 위치에 로봇이 없고, 다음 위치가 내구도가 있는 경우
                remain[r + 1] -= 1  # 내구도 감소
                if not remain[r + 1]: 
                    zeroCount += 1
                if r + 1 == downCursor or r + 1 == downCursor - (2*N):
                    continue
                robot.append(r+1) # 새로운 위치에 로봇 배치
                judge[r+1] = True

            else: # 다음 위치에 로봇이 있거나, 내구도가 없는 경우
                robot.append(r)
                judge[r] = True

    # 2. 올리는 위치에 있는 칸의 내구도가 0이 아니면, 로봇을 올린다.
    if remain[upCursor]:
        remain[upCursor] -= 1
        if remain[upCursor] == 0:
            zeroCount += 1
        robot.append(upCursor)
        judge[upCursor] = True

    # 3. 해당 단계를 마무리 한다.
    depth += 1

print(depth)