# 풀이 시간: 1시간 30분 + 1시간
# 시간복잡도: O(N^2)
# 공간복잡도: O(N)
# 유형: dfs, bfs
# 참고: https://data-flower.tistory.com/105

# 1)한 번에 순환선에 해당하는 역들을 모두 찾는 것이 아니라, 2)각 역이 순환선에 포함되는지 체크하는 것이 포인트인 듯하다.
# 접근을 1)에 초점을 맞추어 계속 생각했던 점,
# 이후 2)로직으로 풀어야 한다는 것을 알았지만 "dfs가 아닌 bfs로 풀 수 있지 않을까?" 하는 생각에 시간을 오래 잡아먹었다..
    # 결과는 안된다.
    # bfs는 인접 노드를 전부 방문하면서 빈틈없이 방문하는 플로우인데, 그렇게 되면 '1-2-1' 순환 방지를 위한 로직을 적용할 수 없게 된다.
# visited 공간복잡도를 줄이기 위해 백트래킹과 같이 visited[]를 초기화하는 작업에서도 오랜만에 사용하려하니 시간이 걸렸다.


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

# O(N+2N): 정점 N개, 간선 2N개
# start역이 순환선의 역인지 판단하는 함수
def judgeCycleNode(start, now, depth):
    for next in graph[now]:
        # 방문했지만, 시작노드로 돌아오는 순환선일 경우
        # depth >= 2 는 '1-2-1'이 되지 않도록 하기 위함이다.
        if next == start and depth >= 2:
            return True

        # 미방문 노드만 방문
        if not visited[next]:
            visited[next] = True

            # 순환 노드를 찾았을 때는 바로 반환
            if judgeCycleNode(start, next, depth + 1):
                visited[next] = False
                return True

            visited[next] = False

# O(K + 2N): 정점 K개(순환석 역), 간선 2N개
# 순환선에서 각 역까지의 거리를 구하는 함수
def findDistance():
    q = deque()

    # 1. 순환역 인근 역들의 거리를 구하기 위해, 순환역만 큐에 넣도록 한다.
    for i in range(1, N+1):
        if result[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for next in graph[now]:
            if result[next] == float('inf'): # 순환선이 아닐 경우
                q.append(next)
                result[next] = result[now] + 1



# 역의 개수
N = int(input())
# 역들의 연관관계를 표현하기 위한 리스트
graph = [[] for _ in range(N+1)]
# 순환역을 찾을 때, 해당 역을 방문했는지 체크하기 위한 방문 리스트 (방문했으나 depth가 2인 경우 순환역)
visited = [False] * (N + 1)
# 각 역에서 순환선까지의 거리 리스트
result = [float('inf') for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b) # 양방향 관계
    graph[b].append(a)

# 각 역이 순환선의 역인지 판단하기
for i in range(1, N+1):
    visited[i] = True
    if judgeCycleNode(i, i, 0):
        result[i] = 0
    visited[i] = False

# 각 역과 순환선 사이의 거리 구하기
findDistance()

for i in range(1, N+1):
    print(result[i], end=" ")