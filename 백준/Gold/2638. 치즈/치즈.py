# 풀이 시간 : 38분
# 시간복잡도 : O(4NM * a)
# 공간복잡도 : O(NM)
# 참고 : -

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1: # 치즈와 맞닿아 있는 공기 면의 개수 측정
                visited[nx][ny] += 1

            if not visited[nx][ny]:
                visited[nx][ny] += 1
                dfs(nx, ny)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

time = 0
while True:
    time += 1
    loop = False

    visited = [[0 for _ in range(M)] for _ in range(N)]
    dfs(0, 0)

    for i in range(N):
        for j in range(M):
            # 치즈 블록이 외부 공기 면과 2면 이상이 접촉하면 녹는다.
            if board[i][j] == 1 and visited[i][j] >= 2:
                loop = True
                board[i][j] = 0

    # 더 이상 녹는 치즈가 없다면 종료
    if not loop:
        break

# 1번의 무의미한 반복이 생겼으므로 -1
print(time-1)