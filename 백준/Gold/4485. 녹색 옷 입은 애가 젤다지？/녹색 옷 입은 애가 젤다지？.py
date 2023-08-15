import heapq
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = float('inf')

def dijkstra():
    q = []
    heapq.heappush(q, (0,0))
    result[0][0] = matrix[0][0]

    while q:
        x, y = heapq.heappop(q)

        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #유효한 인덱스일 때
            if 0<=nx<N and 0<=ny<N:
                #최소 cost만 저장한 result / 이전 최소 + 입력값 비교
                if result[nx][ny] > result[x][y] + matrix[nx][ny]:
                    result[nx][ny] = result[x][y] + matrix[nx][ny]
                    heapq.heappush(q, (nx, ny))

num = 1
while True:
    #행,열 크기
    N = int(input())
    if N==0:
        break

    #그래프 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [[INF] * N for _ in range(N)]

    dijkstra()
    print(f"Problem {num}: {result[N - 1][N - 1]}")
    num+=1;