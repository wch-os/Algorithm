# dfs 풀이 : 시작점 (0,0)에 경로 횟수가 저장됨
# 이전 제출 코드의 문제점
   # 1. dp 중복을 거르지 않았다.
   # 2. dp 초기화를 0으로 했다.
      # '0'으로 하면 시간초과가 난다.
      # Why?
        # 경로가 없을 경우에는 DP[][]에 0이 저장될 것이다.
        # 이런 경우에 탐색을 하였어도, 0이 저장되었으므로 재탐색을 할 것이다.

# dfs에서의 dp 정의 : (x,y)에서 도착지점까지 갈 수 있는 경로의 개수
# bfs에서의 dp 정의 : 출발지점에서 (x,y)까지 갈 수 있는 경로의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    if x == a-1 and y == b-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0 # 탐색했다는 표시
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 낮은 높이로 이동이 가능하면, queue에 넣음.
        if 0 <= nx < a and 0 <= ny < b and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]



a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]
dp = [[-1] * b for _ in range(a)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(dfs(0, 0))

# q = []
# heapq.heappush(q, [-arr[0][0] ,0, 0])
# while q:
#     trash ,x, y = heapq.heappop(q)
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         # 낮은 높이로 이동이 가능하면, queue에 넣음.
#         if 0 <= nx < a and 0 <= ny < b and arr[x][y] > arr[nx][ny]:
#             # 첫 방문일 경우에만 heap에 넣음.
#               # 탐색시간 줄이기 위해 '이전 경로 수를 더해주는 방식'으로 접근한다.
#             if dp[nx][ny] == 0:
#                 heapq.heappush(q, [-arr[nx][ny], nx, ny])
#
#             dp[nx][ny] += dp[x][y] # 이전 경로 개수를 더해준다.