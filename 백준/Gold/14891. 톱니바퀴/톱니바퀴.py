# 맞닿은 극이 다를 경우, 반대 방향으로 회전
# 문제는 1번째 바퀴, 풀이는 0번째 바퀴
# 31번째 라인에서 실수;; 꼼꼼히 보자

import sys
from collections import deque
input = sys.stdin.readline

def leftMove(idx, direction):
    if idx == 0:
        return

    # 왼쪽
    if bike[idx][-2] != bike[idx - 1][2]:
        leftMove(idx - 1, -direction) # 왼쪽 방향으로 0번째 바퀴까지
        rotateDir[idx - 1] = -direction # 방향 저장

def rightMove(idx, direction):
    if idx == 3:
        return

    # 오른쪽
    if bike[idx][2] != bike[idx + 1][-2]:
        rightMove(idx + 1, -direction) # 오른쪽 방향으로 3번째 바퀴까지
        rotateDir[idx + 1] = -direction # 방향 저장

# 모든 바퀴 한 번에 rotate 하기
def concurrentRotate():
    for i in range(4):
        if rotateDir[i]:
            bike[i].rotate(rotateDir[i])

# 점수 계산하기
def calculate():
    global result

    for i in range(4):
        if bike[i][0]:
            result += (2 ** i)


bike = deque(deque(map(int, input().strip())) for _ in range(4))
K = int(input())
for k in range(K):
    rotateDir = [0, 0, 0, 0]
    i, d = map(int, input().split())

    rotateDir[i-1] = d
    leftMove(i-1, d)
    rightMove(i-1, d)

    concurrentRotate()

result = 0
calculate()

print(result)