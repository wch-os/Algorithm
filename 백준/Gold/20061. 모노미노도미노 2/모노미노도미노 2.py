# 1. 0번째 라인 '0' 초기화가 필요
# 2. 0/1번째 블록 판단보다, 밑칸에 1줄칸이 채워져있는지 먼저 확인해야 한다.
# 3. 0번째 라인 '0' 초기화를 다 내리고, 마지막에 해야 한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 블루/그린 보드판에 블럭 배치하기
def move(t, x, y):
    # t = 1, (x, y)
    if t == 1:
        # 블루, 행 고정 → 뒤집었으니 열 고정
        k = one(blue, x)
        blue[k][x] = 1

        # 그린, 열 고정
        l = one(green, y)
        green[l][y] = 1

    # t = 2, (x, y) / (x, y+1) ㅡ
    elif t == 2:
        k = two(blue, x, 1)
        blue[k][x] = 1
        blue[k-1][x] = 1

        l = two(green, y, 2)
        green[l][y] = 1
        green[l][y+1] = 1

    # t = 3, (x, y) / (x+1, y) ㅣ
    elif t == 3:
        k = two(blue, x, 2)
        blue[k][x] = 1
        blue[k][x+1] = 1

        l = two(green, y, 1)
        green[l][y] = 1
        green[l-1][y] = 1

    check(blue)
    check(green)


# 블록 내리기 위한 좌표 찾기 : .
def one(board, fix):
    for i in range(6):
        if board[i][fix]:  # 이미 채워져 있으면
            return i - 1
    return i

# 블록 내리기 위한 좌표 찾기 : ㅡ, ㅣ
def two(board, fix, d):
    dirs = [(0, 0), (1, 0), (0, 1)]

    for i in range(6):
        if i + dirs[d][0] < 6 and fix + dirs[d][1] < 4:
            if board[i + dirs[d][0]][fix + dirs[d][1]]:  # 칸에 이미 블럭이 있는 경우
                return i + dirs[d][0] - 1
        if board[i][fix]:
            return i - 1

    return i


# 블록을 내렸을 때 사라지는 블록이 있는지 체크하기
def check(board):
    # 0/1번째 블록 판단보다, 밑칸에 1줄칸이 채워져있는지 먼저 확인해야 한다.
    for i in range(5, -1, -1):
        flag = True
        for j in range(4):
            if board[i][j]: # 블럭 o
                if i == 0 or i ==1:
                    down(5, board, False)
            else: # 블럭 x
                flag = False

        if flag:
            down(i, board, True)


# 블록이 사라졌을 때, 전체 내리기
def down(k, board, scoreJ):
    global score
    if scoreJ:
        score += 1

    for i in range(k-1, -1, -1):
        for j in range(4):
            board[i+1][j] = board[i][j]

    # 0번째 라인 '0' 초기화가 필요, 0번째 줄은 초기화되지 않는다.
    # ex) board[1][0] = board[0][0]
    for j in range(4):
        board[0][j] = 0

    check(board)



if __name__ == "__main__":
    N = int(input())
    score = 0
    debug = 0
    blue = [[0] * 4 for _ in range(6)]
    green = [[0] * 4 for _ in range(6)]
    for _ in range(N):
        debug += 1
        t, x, y = map(int, input().split())
        move(t, x, y)

    block = 0
    for i in range(6):
        for j in range(4):
            if blue[i][j]:
                block += 1
            if green[i][j]:
                block += 1

    print(score)
    print(block)