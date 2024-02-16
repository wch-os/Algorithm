# 풀이 시간 : 35분 + 30분?
# 시간복잡도 : O(2NM)
# 공간복잡도 : O(NM)
# 참고 : -

# dfs, bfs를 해서 모든 지역을 방문하자
    # 시작점에 따라 결과가 달라짐
        # 그러면, "연결됨"을 파악하자
        # L, R에서는 좌우 블록을 dfs 탐색
        # U, D에서는 상하 블록을 dfs 탐색

# 총 몇 번 방문하는지 파악

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, idx):
    global result

    # 이미 표식이 있는 블록이면
    if visited[x][y] != -1:
        if visited[x][y] == idx:
            result += 1
        return

    visited[x][y] = idx # 표식
    k = direction.index(board[x][y])
    dfs(x + dx[k], y + dy[k], idx)



N, M = map(int, input().split())
board = [input() for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

result = 0
dfsCount = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            dfsCount += 1
            dfs(i, j, dfsCount)

# print(dfsCount)
print(result)