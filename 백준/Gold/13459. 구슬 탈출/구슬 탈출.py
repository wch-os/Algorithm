# 풀이 시간: 45분
# 시간복잡도: O(4* a^2)
    # a: '.'의 개수
    # a^2: R, B의 위치로 중복 노드를 파악함.
# 공간복잡도: O(N^2)
# 유형: bfs, simulation
# 참고: 스터디


import sys
from collections import deque
input = sys.stdin.readline

def move(x, y, i, board):
    count = 0
    while board[x + dx[i]][y + dy[i]] != '#' and board[x][y] != 'O':
        x += dx[i]
        y += dy[i]
        count += 1

    return x, y, count


def bfs(rx, ry, bx, by, board):
    q = deque([(rx, ry, bx, by, 0)]) # 리스트 주의
    visited = set([(rx, ry, bx, by)])

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth >= 10:
            return 0

        for i in range(4):
            move_rx, move_ry, red_count = move(rx, ry, i, board)
            move_bx, move_by, blue_count = move(bx, by, i, board)

            """빨간색 구슬만 빼낼 수 있을 때"""
            if board[move_bx][move_by] == 'O':
                continue
            elif board[move_rx][move_ry] == 'O':
                return 1

            """빨간 구슬과 파란 구슬이 동시에 같은 칸이 있을 경우"""
            if move_rx == move_bx and move_ry == move_by:
                if red_count > blue_count:
                    move_rx -= dx[i]
                    move_ry -= dy[i]
                else:
                    move_bx -= dx[i]
                    move_by -= dy[i]

            """중복 분기 탐색 X"""
            if (move_rx, move_ry, move_bx, move_by) not in visited:
                visited.add((move_rx, move_ry, move_bx, move_by))
                q.append((move_rx, move_ry, move_bx, move_by, depth + 1))

    return 0


def init():
    N, M = map(int, input().split())  # 세로, 가로
    board = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j

    print(bfs(rx, ry, bx, by, board))


if __name__ == "__main__":
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]

    init()