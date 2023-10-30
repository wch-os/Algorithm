# 풀이 시간 : 1시간 10분 + 1시간 30분
# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n^2)
# 참고 아이디어 : https://jisunshine.tistory.com/183
    # visited를 boolean으로 정의하고 풀 시, 우산을 획득하고 지나가는 효율적인 경로를 고려하지 못하게 된다.

import sys
from collections import deque

input = sys.stdin.readline

# N : 정사각현 한 번, H : 현재 체력, D : 우산의 내구도
N, H, D = map(int, input().split())

# U : 우산, S : dkswjswleo, . : 빈칸
ary = [list(map(str, input().rstrip())) for _ in range(N)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

ulist = []
for i in range(N):
    for j in range(N):
        if ary[i][j] == 'S':
            sx = i
            sy = j

        elif ary[i][j] == 'E':
            ex = i
            ey = j

q = deque()
q.append((sx, sy, H, 0, 0)) # 시작 좌표 x/y, 체력, 이동 거리, 우산 사이 걷는 거리
visited = [[0] * N for _ in range(N)] # 해당 지점에서 남은 체력
visited[sx][sy] = H

umbrella = False
while len(q)>0:
    x, y, power, dis, interval = q.popleft()

    # end 지점 도착
    if x == ex and y == ey:
        print(dis)
        exit()

    # 우산 도착
    if ary[x][y] == 'U':
        if umbrella: # 이전에 우산이 있는 상태
            if interval < D: # 우산 내구도가 남아있는 상태에서, 새로운 우산을 썼을 때
                power = power - (D - interval) # 남은 내구도 빼주기
        power += D
        interval = 0
        umbrella = True

    # 현재 체력을 다 소비하면
    if power == 0:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if power > visited[nx][ny]: # 현재 목숨 + 우산의 내구도의 합이 더 큰 경우
                visited[nx][ny] = power
                q.append((nx, ny, power-1, dis+1, interval+1))

print(-1)