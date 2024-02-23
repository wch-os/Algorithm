# 풀이 시간 : 1시간 20분 + 30분
# 시간복잡도 : O(3(V+E))
# 공간복잡도 : O(N)
# 참고 : -

# s → c 경로 거리와
    # (s → g → h → c) , (s → h → g → c) 가 일치하는지 확인한다.
    # 일치하면 최단 경로에서 g-h 교차로를 지나가고 있는 것이다.

# 틀린 이유
    # 시작지에서 도착지까지 경로가 여러개 있을 경우 찾지 못한다..
    # INF = float('inf') 로 했을 경우
        # s → c 까지의 경로가 없을 때 INF
        # (s → g → h → c) , (s → h → g → c) 또한 INF 로
        # g-h 교차로를 지나가고 목적지에 도착했다고 판단한다.

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # 기존 저장되어 있는 것이 더 작다면
        if distance[now] < dist:
            continue

        for next_dist, next_node in graph[now]:
            if distance[next_node] > distance[now] + next_dist:
                distance[next_node] = distance[now] + next_dist
                heapq.heappush(pq, (distance[next_node], next_node))

    return distance


T = int(input())
for _ in range(T):
    # 교차로, 도로, 목적지 후보의 개수
    N, M, t = map(int, input().split())

    # 범인 출발 위치, g와 h 사이 지나감
    s, g, h = map(int, input().split())

    # 도로 그리기
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

        if (a == g and b == h) or (a == h and b == g):
            gToh = c

    # 목적지 후보 리스트
    candidates = [int(input()) for _ in range(t)]

    distFromS = dijkstra(s)
    distFromG = dijkstra(g)
    distFromH = dijkstra(h)

    result = []
    for c in candidates:
        # s → c
        K = distFromS[c]

        # (s → g → h → c) , (s → h → g → c)
        minS = min(distFromS[g] + gToh + distFromH[c], distFromS[h] + gToh + distFromG[c])

        # 기존 최단거리에서 g-h 교차로를 지나갔음을 의미한다..
        if K == minS:
            result.append(c)

    result.sort()
    print(*result)