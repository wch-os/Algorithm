# 풀이 시간 : 1시간 30분 + 1시간 30분
# 시간복잡도 : O(RC + RC)
    # 도보 + 말
# 공간복잡도 : O(RCK)
# 참고 : https://velog.io/@thguss/%EB%B0%B1%EC%A4%80-1600.-%EB%A7%90%EC%9D%B4-%EB%90%98%EA%B3%A0%ED%94%88-%EC%9B%90%EC%88%AD%EC%9D%B4-with.-Python

import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
C, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

# visited[row][col][K]
# 각 (r, c)까지 도착했을 때, 말 동작을 몇 번 수행했는가?
# visited[0][0][0]을 0 설정 위해 '-1'로 초기화
visited = [[[-1] * (K+1) for _ in range(C)] for _ in range(R)]

# 일반 동작
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 말 동작
horseDx = [-2,-2,-1,-1,1,1,2,2]
horseDy = [-1,1,-2,2,-2,2,-1,1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0)) # (0, 0) 시작, K번 말 동작 가능
    visited[0][0][0] = 0 # (0, 0, 0) 은 이동횟수 '0'

    while queue:
        x, y, k = queue.popleft()

        # 도착 지점에 빠르게 온 경우가 있다면, 그대로 출력
        if x == R-1 and y == C-1:
            return visited[x][y][k]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 유효 범위 & 갈 수 있는 길 & 도보, 말 동작 경우에서 방문한 적 없는 길
            if (0 <= nx < R and 0 <= ny < C) and (graph[nx][ny] == 0) and (visited[nx][ny][k] < 0):
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx, ny, k))


        # K번 동작을 수행하면, 더 이상 말 동작 x
        if k < K:
            for i in range(8):
                nx = x + horseDx[i]
                ny = y + horseDy[i]

                # 유효 범위 & 갈 수 있는 길 & 도보, 말 동작 경우에서 방문한 적 없는 길
                # 말 동작 1회 count
                if (0 <= nx < R and 0 <= ny < C) and (graph[nx][ny] == 0) and (visited[nx][ny][k+1] < 0):
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k+1))

    return -1

print(bfs())