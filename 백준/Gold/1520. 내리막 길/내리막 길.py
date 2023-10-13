# 참고 : https://velog.io/@nathan29849/BAEKJOON-1520-%EB%82%B4%EB%A6%AC%EB%A7%89-%EA%B8%B8-DFS-BFS-python

# bfs를 사용할 때 "deque이 아닌 PriortyQueue를 사용해야 하는 이유"
   # deque을 쓰면, 돌아가는 경로에서 제대로 dp[][] 반영이 되지 않는다.
   # 높이를 기준으로 한 최소힙을 써야 한다.

import heapq
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]
dp = [[0] * b for _ in range(a)]
dp[0][0] = 1

q = []
heapq.heappush(q, [-arr[0][0] ,0, 0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    trash ,x, y = heapq.heappop(q)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 낮은 높이로 이동이 가능하면, queue에 넣음.
        if 0 <= nx < a and 0 <= ny < b and arr[x][y] > arr[nx][ny]:
            # 첫 방문일 경우에만 heap에 넣음.
              # 탐색시간 줄이기 위해 '이전 경로 수를 더해주는 방식'으로 접근한다.
            if dp[nx][ny] == 0:
                heapq.heappush(q, [-arr[nx][ny], nx, ny])

            dp[nx][ny] += dp[x][y] # 이전 경로 개수를 더해준다.

print(dp[a-1][b-1])