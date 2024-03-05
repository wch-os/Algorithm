# 풀이 시간 : 12분
# 시간복잡도 : O(K*4)
    # K : 배추 개수
    # 4 : 노드 개수
# 공간복잡도 : O(NM)
# 참고 : -

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if farm[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    farm = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        farm[x][y] = 1


    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    result = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]:
                result += 1
                visited[i][j] = True
                dfs(i, j)

    print(result)