from collections import deque

#사용하는 자료구조
graph = []
queue = deque()

#상하좌우 탐색
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        y, x = queue.popleft()

        #익은 토마토를 중심으로, 상하좌우 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=nx<M and 0<=ny<N:
                #주변 토마토가 익지 않았다면, 체크
                if graph[ny][nx]==0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((ny, nx)) #익은 토마토를 중심으로 재탐색


#상자의 크기(가로, 세로)
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))

bfs()

not_complete = False #상자의 토마토 중 익지 않은 것이 있을 경우, True
day = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            not_complete = True

        day = max(day, graph[i][j]) #BFS 최소 탐색 횟수 = 토마토가 모두 익을 때까지의 최소 날짜 

if not_complete:
    print(-1)
else:
    print(day-1)
