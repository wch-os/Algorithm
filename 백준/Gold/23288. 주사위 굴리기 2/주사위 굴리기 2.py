# 문제에서 5-앞면, 2-뒷면이다.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, num):
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True

    q = deque()
    q.append((x, y))
    cnt = 1
    while q:
        a, b = q.popleft()

        for i in range(4):
            na = a + da[i]
            nb = b + db[i]

            if 0 <= na < N and 0 <= nb < M:
                if not visited[na][nb] and board[na][nb] == num:
                    visited[na][nb] = True
                    q.append((na, nb))
                    cnt += 1

    return num * cnt

# 윗, 앞, 오, 왼, 뒷, 밑
dice = [0, 1, 5, 3, 4, 2, 6]
def changeDir(d):
    if d == 0: # 동쪽
        dice[6], dice[1], dice[4], dice[3] = dice[3], dice[4], dice[6], dice[1]
    elif d == 1: # 남쪽
        dice[6], dice[5], dice[1], dice[2] = dice[2], dice[6], dice[5], dice[1]
    elif d == 2: # 서쪽
        dice[6], dice[1], dice[4], dice[3] = dice[4], dice[3], dice[1], dice[6]
    else: # 북쪽
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1] # 동남서북
dy = [1, 0, -1, 0]
x, y, d = 0, 0, 0 # 시작 위치, 방향(동쪽)

result = 0
for k in range(K):
    # 1. 범위 바깥일 경우, 방향 리버스
    if 0 > x + dx[d] or N <= x + dx[d] or 0 > y + dy[d] or M <= y + dy[d]:
        d = (d + 2) % 4
    nx = x + dx[d]
    ny = y + dy[d]


    # 2. 현재 노드 숫자와 같은 값 찾기
    result += bfs(nx, ny, board[nx][ny])

    # 3. 현재 노드 숫자와 주사위 밑면 비교해서 방향 바꿔주기
    changeDir(d)
    under = dice[6]
    if board[nx][ny] < under:
        d = (d + 1) % 4
    elif board[nx][ny] > under:
        d = (d - 1) % 4

    x = nx
    y = ny

print(result)