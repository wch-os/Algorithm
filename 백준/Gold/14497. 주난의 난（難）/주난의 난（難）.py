# 풀이 시간: 40분 + 15분
# 시간복잡도: O(NM * log(NM))
# 공간복잡도: O(NM)
# 유형: 다익스트라, 그래프 탐색

# board[x][y] = 0일 때는 cost 소모 없이 이동
# board[x][y] = 1일 때는 cost + 1 소모를 하도록 하여
# heap을 활용한 다익스트라 알고리즘을 통해, cost가 가장 적은 노드부터 탐색하도록 한다.

# 1) 31번째 라인에서 재방문 간선의 처리가 되므로 이전 코드의 visited 배열은 필요가 없다.
# 2) 최소 간선을 갱신하기 위해서 minDistance[nx][ny]와 cost를 비교할 것이 아니라 (완전히 잘못됨)
    # 현재 최소 cost가 저장된 minDistance[nx][ny]와 지금 minDistnace[nx][ny] + a 를 비교해주었어야 했다.

import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    minDistance = [[float('inf')] * M for _ in range(N)]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    q = []
    heapq.heappush(q, (0, x1, y1))
    minDistance[x1][y1] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == x2 and y == y2:
            break

        if minDistance[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                nextCost = cost + (board[nx][ny] == "1")

                if minDistance[nx][ny] > nextCost: # 기존의 간선을 최소 비용 간선으로 갱신
                    heapq.heappush(q, (nextCost, nx, ny))
                    minDistance[nx][ny] = nextCost

    return minDistance[x2][y2] + 1 # "#"일 때에도 빈 공간과 마찬가지로 cost를 유지하였기 때문에 +1을 해주도록 한다.



N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

board = [list(input()) for _ in range(N)]

print(dijkstra())