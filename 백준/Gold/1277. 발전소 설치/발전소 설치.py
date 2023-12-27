# 수정
    # 각 발전소까지 거리 구할 때, 최적화 함.
    # w, 주어진 간선에서 단방향 간선으로 작성함... #57번째 라인


# 풀이 시간 : 1시간 10분 + 30분
# 시간복잡도 : O(N^2 * logE)
    # ElogE → 2ElogN → ElogN → N^2 * logN
# 공간복잡도 : O(N^2)
# 참고 : 아이디어, https://sumin-kim-dev.github.io/boj/boj-gold-1277/

# 구하고자 하는 것
    # 1번 발전소와 N번 발전소를 잇는데 필요한 추가 전선 길이의 최솟값 * 1000

# 초기 접근법
    # 1. 1번 발전소에서 N번 발전소까지만 가면 된다.
        # 즉, "1"에서 "N"까지의 최소 경로를 구해야 하므로, 다익스트라 알고리즘을 사용한다.
    # 2. 추가 전선의 길이가 최소가 되게끔 이동한다.
        # 이 때, 두 발전소 사이의 전선 길이가 M을 초과해서는 안된다.

    # 2차원 좌표를 그래프로 표현하면 공간 복잡도가 100억이 나오므로 불가능 (bfs, dfs X)
    # 그러면 "graph[N][N] = 각 발전소까지의 거리"는 할 수 있겠다.
        # 만약 0인 경우, 지금까지 visited[] = True 노드를 M 범위 탐색
        # result[0_Node] 에 필요한 추가 전선 길이의 최솟값 저장함
            # result[0_Node] = min(result[0_Node], sqrt((dot[i][x] - dot[j][x])^2 + (dot[i][y] - dot[j][y])^2))
        # 우선순위 큐에는 result[0_Node] 가 작은 것을, 즉 추가 전선 길이의 최솟값이 작은 것을 먼저 뺀다.



import heapq
import math
import sys
input = sys.stdin.readline

# N : 발전소의 수, M : 현재 남아있는 전선의 수
N, W = map(int, input().split())

# 제한 길이
M = float(input())

# graph[i][j] = x
    # i 발전소에서 j 발전소까지의 전선 길이는 x
graph = [[] for _ in range(N+1)]
# 각 발전소에 도착하기까지 필요한 추가 전선 길이의 최솟값을 저장한다.
minDistance = [float('inf')] * (N+1)

# 각 발전소의 X, Y 좌표
dot = [(0, 0)]
for i in range(N):
    X, Y = map(int, input().split())
    dot.append((X, Y))

# 현재 남아있는 전선이 잇고 있는 두 발전소
for _ in range(W):
    a, b = map(int, input().split())
    graph[a].append((0, b)) # 남아있는 전선 활용 : 0
    graph[b].append((0, a))


# 각 발전소(노드)끼리의 거리(간선) 정의
for i in range(1, N+1):
    for j in range(i+1, N+1):
        # dis : 노드 간의 거리
        dis = ((dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2 ) ** 0.5
        if dis <= M:
            graph[i].append((dis, j)) # 양방향
            graph[j].append((dis, i))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    minDistance[1] = 0 # 시작노드, 필요 추가 전선은 '0'

    while q:
        dist, node = heapq.heappop(q)

        # 이미 갱신된 거리보다 클 시, pass
        if minDistance[node] < dist:
            continue

        for next_dist, next_node, in graph[node]:
            cost = minDistance[node] + next_dist

            if minDistance[next_node] > cost:
                minDistance[next_node] = cost
                heapq.heappush(q, (cost, next_node)) # 노드까지의 최소 비용이 갱신되었다면, 우선순위 큐에 삽입

dijkstra()

# 1번 발전소에서, N번 발전소까지 가는 데 필요한 최소 전선
print(int(minDistance[N]*1000))