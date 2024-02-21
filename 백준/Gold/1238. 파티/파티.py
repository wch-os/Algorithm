# 풀이 시간 : 13분 + 40분
# 시간복잡도 : O(MlogN*N)
    # N : 현재 노드와 연결된 간선 수 (최대 N임)
    # logM : 간선 heap 추출
    # N : N개 노드에서 다익스트라 해야 함.
# 공간복잡도 : O(N^2)
# 참고 : -

# 플로이드 : O(N^3) = 10억

import heapq
import sys
input = sys.stdin.readline

def dijkstra(i):
    pq = []
    heapq.heappush(pq, (0, i))
    distance = [float('inf')] * (N + 1)
    distance[i] = 0

    while pq:
        cost, now = heapq.heappop(pq)

        # 기존에 저장(갱신)된 있는 cost가, heap에 저장된 cost보다 더 작으면 고려할 필요가 없다.
        if distance[now] < cost:
            continue

        for next_cost, next_node in graph[now]:
            # 현재 테이블에 저장된 비용 vs now까지 오는 비용 + now에서 next_node까지 가는 비용
            if distance[next_node] > distance[now] + next_cost:
                distance[next_node] = distance[now] + next_cost
                heapq.heappush(pq, (distance[now] + next_cost, next_node))

    return distance


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 단방향 그래프 그리기
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

# x에서 i까지의 소요시간
xToi_Distance = dijkstra(X)

result = 0 # 가장 오래 걸리는 학생의 소요시간
for i in range(1, N+1):
    if i == X:
        continue

    # i에서 x까지의 소요시간
    iTox_Distance = dijkstra(i)
    result = max(result, iTox_Distance[X] + xToi_Distance[i])

print(result)