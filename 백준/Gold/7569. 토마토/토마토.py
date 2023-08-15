import sys
from collections import deque

#사용하는 자료구조
graph = []
queue = deque()

def bfs():
    while queue:
        z, y, x = queue.popleft() #큐로 사용

        # 상하좌우, 높이 6군데 탐색
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1  # BFS 최소 탐색 횟수를 찾기 위함
                    queue.append((nz, ny, nx))

#그래프 6곳 탐색
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]

#가로, 세로, 높이 입력
M, N, H = map(int, input().split())

#3차원 배열 생성
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

#익은 토마토 queue에 삽입
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs()

not_complete = False #True : 모두 익지 않은 상태
day = 1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0: #익지 않은 토마토 발견
                not_complete = True
            day = max(day, graph[i][j][k]) #BFS 최소 탐색 횟수

if not_complete:
    print(-1)
else:
    print(day-1)