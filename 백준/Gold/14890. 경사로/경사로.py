import sys
input = sys.stdin.readline

def rowSearch():
    result = []
    possible = 0

    for i in range(N):
        setTry = True # 경사로를 설치할 수 있는지 판단
        setBoard = [] # 경사로를 설치할 좌표를 담는 공간
        for j in range(N-1):
            if abs(board[i][j] - board[i][j+1]) >= 2:
                setTry = False
                break

            elif board[i][j] > board[i][j+1]: # 기존 높이가 큰 경우
                for k in range(j+1, j+1+L): # 경사로 길이와 맞는지 판단
                    if k >= N or board[i][j+1] != board[i][k] or visited[i][k]: # 이미 경사로가 설치되어 있으면
                        setBoard.clear()
                        setTry = False
                        break
                    else:
                        setBoard.append((i, k))


            elif board[i][j] < board[i][j + 1]: # 기존 높이가 낮은 경우
                for k in range(j, j-L, -1):
                    if k < 0 or board[i][j] != board[i][k] or visited[i][k]:
                        setBoard.clear()
                        setTry = False
                        break
                    else:
                        setBoard.append((i, k))

            # 경사로 설치 불가능
            if not setTry:
                break
            # 경사로 설치
            else:
                for r, c in setBoard:
                    visited[r][c] = True


        # 한 행의 검사가 모두 끝나고, 경사로를 설치할 수 있으면
        if setTry:
            result.append(i)
            possible += 1
        else: # 해당 행 visited False로 초기화
            for col in range(N):
                visited[i][col] = False

    return possible


def colSearch():
    result = []

    possible = 0

    for j in range(N):
        setTry = True  # 경사로를 설치할 수 있는지 판단
        setBoard = []  # 경사로를 설치할 좌표를 담는 공간
        for i in range(N - 1):
            if abs(board[i][j] - board[i+1][j]) >= 2:
                setTry = False
                break

            if board[i][j] > board[i+1][j]:  # 기존 높이가 큰 경우
                for k in range(i + 1, i + 1 + L):  # 경사로 길이와 맞는지 판단
                    if k >= N or board[i+1][j] != board[k][j] or visited[k][j]: # 이미 경사로가 설치되어 있으면
                        setBoard.clear()
                        setTry = False
                        break
                    else:
                        setBoard.append((k, j))


            elif board[i][j] < board[i + 1][j]: # 기존 높이가 낮은 경우
                for k in range(i, i - L, -1):
                    if k < 0 or board[i][j] != board[k][j] or visited[k][j]:
                        setBoard.clear()
                        setTry = False
                        break
                    else:
                        setBoard.append((k, j))

            # 경사로 설치 불가능
            if not setTry:
                break
            # 경사로 설치
            else:
                for r, c in setBoard:
                    visited[r][c] = True

        # 한 행의 검사가 모두 끝나고, 경사로를 설치할 수 있으면
        if setTry:
            result.append(j)
            possible += 1
        else: # 해당 열 visited False로 초기화
            for row in range(N):
                visited[row][j] = False

    return possible


# 맵 크기, 경사로 길이
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
rA = rowSearch()

visited = [[False] * N for _ in range(N)]
rB = colSearch()

print(rA + rB)