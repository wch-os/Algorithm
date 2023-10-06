# graph를 foreach문으로 만들면서, graph 탐색 시간을 줄여줬다.

import heapq
import sys
input = sys.stdin.readline

def prim():
    global result

    while q:
        # 미방문 노드가 나올 때까지 pop
        minCost, start = heapq.heappop(q)

        if visited[start]:
            continue

        visited[start] = True # 방문처리
        result += minCost # MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점 선택
        
        for node, cost in graph[start]:
            if not visited[node]: # 미방문 노드이면
                heapq.heappush(q, (cost, node)) # cost와 노드 push



N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결할 수 있는 선의 수

graph = [[] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 입력값으로 그래프 만들기
for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

result = 0 # 모든 컴퓨터를 연결하는데 필요한 최소비용
q = [(0, 1)] # 임의의 정점 (cost, node)
prim()

print(result)