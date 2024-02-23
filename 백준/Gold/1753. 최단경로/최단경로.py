# 풀이 시간 : 10분
# 시간복잡도 : O(V+E)
# 공간복잡도 : O(V)
# 참고 : -

import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
    pq = []
    heapq.heappush(pq, (0, s))
    distance[s] = 0

    while pq:
        time, now = heapq.heappop(pq)

        # 기존에 저장되어 있는 값이 더 작으면
        if distance[now] < time:
            continue

        # 거리 갱신
        for next_time, next_node in graph[now]:
            if distance[next_node] > distance[now] + next_time:
                distance[next_node] = distance[now] + next_time
                heapq.heappush(pq, (distance[next_node], next_node))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [float('INF') for _ in range(V+1)]

for _ in range(E):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == float('INF'):
        print("INF")
    else:
        print(distance[i])