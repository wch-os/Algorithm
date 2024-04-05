import copy
import sys
input = sys.stdin.readline

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 # 먼저 이동을 시키는 전제 하에 0으로 만든다. → 숫자가 이미 있는 경우 cursor + 1 로 제자리에 위치할 수도

                # board[i][cursor] : 옮기려고 하는 공간
                if board[i][cursor] == tmp: # 같은 숫자
                    board[i][cursor] *= 2
                    cursor += 1

                # 좌측에 있는 수와 비교해서 합칠 수도 있기 때문에 cursor를 이동하지 않는다.
                elif board[i][cursor] == 0: # 빈 공간
                    board[i][cursor] = tmp

                else: # 숫자가 이미 있는 경우
                    cursor += 1
                    board[i][cursor] = tmp

    return board


def right(board):
    for i in range(N):
        cursor = N-1
        for j in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                # board[i][cursor] : 옮기려고 하는 공간
                if board[i][cursor] == tmp:  # 같은 숫자
                    board[i][cursor] *= 2
                    cursor -= 1

                elif board[i][cursor] == 0:  # 빈 공간
                    board[i][cursor] = tmp

                else:  # 숫자가 이미 있는 경우
                    cursor -= 1
                    board[i][cursor] = tmp

    return board


def up(board):
    for j in range(N):
        cursor = 0
        for i in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                # board[cursor][j] : 옮기려고 하는 공간
                if board[cursor][j] == tmp:  # 같은 숫자
                    board[cursor][j] *= 2
                    cursor += 1

                elif board[cursor][j] == 0:  # 빈 공간
                    board[cursor][j] = tmp

                else:  # 숫자가 이미 있는 경우
                    cursor += 1
                    board[cursor][j] = tmp

    return board


def down(board):
    for j in range(N):
        cursor = N-1
        for i in range(N-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                # board[cursor][j] : 옮기려고 하는 공간
                if board[cursor][j] == tmp:  # 같은 숫자
                    board[cursor][j] *= 2
                    cursor -= 1

                elif board[cursor][j] == 0:  # 빈 공간
                    board[cursor][j] = tmp

                else:  # 숫자가 이미 있는 경우
                    cursor -= 1
                    board[cursor][j] = tmp

    return board


def dfs(depth, board):
    global result

    if depth == 5:
        for row in board:
            result = max(result, max(row))
        return

    for i in range(4):
        copyBoard = copy.deepcopy(board)
        if i == 0:
            dfs(depth+1, left(copyBoard))
        elif i == 1:
            dfs(depth+1, right(copyBoard))
        elif i == 2:
            dfs(depth+1, up(copyBoard))
        else:
            dfs(depth+1, down(copyBoard))


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    dfs(0, board)
    print(result)



# cursor를 사용하는 이유

#             if board[i][j-1] == board[i][j]: # 같은 숫자
#                 board[i][j-1] *= 2
#                 board[i][j] = 0
#             elif board[i][j-1] == 0: # 빈공간
#                 board[i][j-1] = board[i][j]
#                 board[i][j] = 0
#             else: # 숫자가 이미 있는 경우
#                 # 이 때 맨 끝에 있는 걸 가져올 수가 없다.