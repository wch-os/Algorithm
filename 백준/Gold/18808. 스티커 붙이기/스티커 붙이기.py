# 풀이 시간 : 1시간 30분
# 시간복잡도 : O(4*s^2*n^2) / s:스티커, n:노트북
# 공간복잡도 : O(n^2)
# 참고 : -

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
notebook = [[False] * M for _ in range(N)]

# 스티커 붙일 수 있는지 판단
def check(a, b):
    for i in range(a, row + a):
        for j in range(b, col + b):
            if 0 <= i < N and 0 <= j < M:
                # 스티커 영역을 먼저 확인하고, notebook에 붙일 수 있는지 판단하기
                if sticker[i-a][j-b] == 1:
                    if notebook[i][j]:
                        return False

            # 범위 바깥일 시, False
            else:
                return False
            
    return True

# 스티커 붙이기
def attach(a, b):
    for i in range(a, row + a):
        for j in range(b, col + b):
            # 스티커 영역을 먼저 확인하고, notebook에 붙이기
            if sticker[i-a][j-b] == 1:
                notebook[i][j] = True

def rot():
    global sticker
    rotateSticker = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            # 회전된 스티커의 '행' 좌표는, 기존 스티커의 '열' 좌표가 되며
            # '열' 좌표는 '행' 좌표의 대칭점이 된다.
            rotateSticker[j][row - 1 - i] = sticker[i][j]

    sticker = rotateSticker


for p in range(K):
    row, col = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(row)]

    rotate = False # 끝까지 완탐했는데도, 스티커를 못 붙이는 경우 rotate
    rotateCnt = 0 # 회전 4번했는지 판단

    # 스티커 이동
    a = 0
    b = 0
    while True:
        # 스티커 회전
        if rotate and rotateCnt < 4:
            rot()
            row, col = col, row # 회전했으니 row, column 변경
            rotate = False


        # 스티커를 4번 회전했는데도 붙이지 못하면, break
        elif rotate and rotateCnt == 4:
            rotateCnt = 0 # 초기화
            break

        # 스티커를 붙일 수 있으면, 붙이고 다음 스티커 판단
        if check(a, b):
            attach(a, b)
            break

        # 스티커 오른쪽으로 이동,
        b += 1

        # 최우하단일 시, 회전
        if row + a > N and col + b > M:
            a, b = 0, 0  # 초기화
            rotate = True # 회전해라.
            rotateCnt += 1 # 회전 count 세기
            continue

        # 끝까지 이동 시 col을 0으로 초기화 후 row 이동
        if col + b > M:
            a += 1 # 행 이동
            b = 0 # 초기화

cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j]:
            cnt += 1

print(cnt)