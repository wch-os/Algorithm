# 풀이 시간 : 1시간 50분
# 시간복잡도 : O(N^2)
# 공간복잡도 : O(N^2)
# 참고 : -

# 범위를 90도 회전할 때 대칭이동으로 생각해서 풀었다.
# 지금까지 90도 회전문제가 나올 때마다 규칙을 생각해서 풀었는데 대칭 이동으로 외워두고 풀면 빠르게 풀릴 것 같다.
# +. 문제에서 a는 55%가 아닌 "이동하지 못한 모래의 양"으로 소수점 버림을 고려해야 한다.

# 서(x, y)
# 남(-y, -x)
# 동(-x, -y)
# 북(y, x)

import sys
input = sys.stdin.readline

def rangeCheck(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True

    return False

# O(20)
def windSand(x, y, boardY, wind):
    global result

    sand = [  # x 좌표 중심
        [-2, -1, 2],
        [-1, -2, 10], [-1, -1, 7], [-1, 0, 1],
        [0, -3, 5],
        [1, -2, 10], [1, -1, 7], [1, 0, 1],
        [2, -1, 2],
        [0, -2, 0], # 나머지
    ]

    if wind == 1: # ↓
        for i in range(10):
            sand[i][0], sand[i][1] = -sand[i][1], -sand[i][0] # '←' y = -x 대칭
    elif wind == 2: # →
        for i in range(10):
            sand[i][0], sand[i][1] = -sand[i][0], -sand[i][1] # 원점 대칭
    elif wind == 3: # ↑
        for i in range(10):
            sand[i][0], sand[i][1] = sand[i][1], sand[i][0] # y = x 대칭

    sumPlusSand = 0
    for i in range(9):
        # (nx, ny) : 바람에 의해 모래가 이동할 장소
        nx = x + sand[i][0]
        ny = y + sand[i][1]

        plusSand = int(boardY * (sand[i][2] / 100))
        sumPlusSand += plusSand # 이동하는 모래의 양 (소수점 아래는 버린다..!!)
        if rangeCheck(nx, ny):
            board[nx][ny] += plusSand
        else: # 범위 바깥
            result += plusSand

    nx = x + sand[9][0]
    ny = y + sand[9][1]
    if rangeCheck(nx, ny):
        board[nx][ny] += (boardY - sumPlusSand) # 이동하지 않는 모래의 양
    else:
        result += (boardY - sumPlusSand)

#O(N^2)
def move(x, y):
    # ← ↓ → ↑
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    cnt = 0  # 방향 횟수

    while True:
        for i in range(4):
            # ← ↓ →→ ↑↑ ←←← ↓↓↓
            if i == 0 or i == 2:
                cnt += 1

            for _ in range(cnt):
                if x == 0 and y == 0:
                    return

                # (x, y) : x 좌표
                # (nx, ny) : y 좌표
                nx = x + direction[i][0]
                ny = y + direction[i][1]

                # 바람에 의해 모래가 날린다.
                windSand(x, y, board[nx][ny], i)

                x, y = nx, ny


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0
c = N // 2
move(c, c)

print(result)