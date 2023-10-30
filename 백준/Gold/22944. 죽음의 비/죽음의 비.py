# 풀이 시간 : 1시간 10분 + 1시간 30분
# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n^2)
# 참고 아이디어 : https://jisunshine.tistory.com/183
    # visited를 boolean으로 정의하고 풀 시, 우산을 획득하고 지나가는 효율적인 경로를 고려하지 못하게 된다.
    # 우산 내구도를 직관적으로 짠 코드

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
q.append((sx, sy, H+1, 0, 0))
visited = [[0] * N for _ in range(N)] # 해당 지점에서 남은 체력
visited[sx][sy] = H

# "출발지도 비를 맞게 코드를 작성해서, 체력을 +1 해준다."
while len(q)>0:
    # 시작 좌표 x/y, 남은 체력, 이동 거리, 우산 내구도
    x, y, power, dis, umbrella = q.popleft()

    # end 지점 도착
    if x == ex and y == ey:
        print(dis)
        exit()

    # 우산 도착
    if ary[x][y] == 'U':
        umbrella = D  # 우산 내구도 초기화

    # 우산 내구도부터 차감, 없으면 체력이 닳는다.
    if umbrella != 0:
        umbrella -= 1
    else:
        power -= 1

    # 현재 체력을 다 소비하면
    if power == 0:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if power + umbrella > visited[nx][ny]: # 현재 목숨 + 우산의 내구도의 합이 더 큰 경우
                visited[nx][ny] = power + umbrella
                q.append((nx, ny, power, dis+1, umbrella))

print(-1)