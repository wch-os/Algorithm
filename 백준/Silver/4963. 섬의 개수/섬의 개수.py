import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

dx = [-1, 0, 0, 1, -1, -1, 1, 1]
dy = [0, -1, 1, 0, -1, 1, -1, 1]
def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)



while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break

    board = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]

    result = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)