# 풀이 시간 : 28분 + 15분
# 시간복잡도 : O(N^3)
# 공간복잡도 : O(N^2)
# 참고 : -


# 틀린이유
# - 자기 자신으로 돌아오는 방향에 대한 초기화를 해주지 않았다. (graph[i][i] = 0)
# - getItems[] 과정에서 틀린 것 같은데
#   이런.. graph[i][i] = 0 으로 초기화하면서 "graph[i][j] <= M" 과정에서 자기 자신도 같이 더해지므로 그전에 미리 더할 필요가 없었다

# 접근법
# 1. 어느 위치에 떨어지는 것이, 아이템을 가장 많이 얻을 수 있는가?
# 2. 모든 노드에서 간선에 대한 수색 범위를 펼쳐서 아이템을 얻는 개수를 구해야 한다.

# graph[N][N] = 길의 길이
# graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# i에서 j까지 최단 경로를 찾아, graph[i][j]에 저장한다.
# 각 노드 graph[i]를 중심으로 탐색 범위 내에 있는 노드들의 아이템 개수를 센다.

import sys
input = sys.stdin.readline

# n : 지역의 개수 / m : 수색범위 / r : 길의 개수
N, M, R = map(int, input().split())

items = list(map(int, input().split()))
# getItems[i] : 탐색 범위 내에 있는 노드들의 아이템 개수 저장
getItems = [0] * (N+1)

graph = [[float('inf')] * (N+1) for _ in range(N+1)]

# 자신으로 돌아오는 방향은 0 초기화
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(R):
    # a, b : 양끝의 지역 번호 / l : 길의 길이
    a, b, l = map(int, input().split())

    graph[a][b] = l
    graph[b][a] = l


# 플로이드 알고리즘
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
# 탐색 범위 내에 있는 아이템 개수 카운트
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] <= M:
            getItems[i] += items[j-1]

print(max(getItems))