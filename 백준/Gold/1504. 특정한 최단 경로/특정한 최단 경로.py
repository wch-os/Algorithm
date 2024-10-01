# 풀이 시간: 25분
# 시간복잡도: O(N^2)
# 공간복잡도: O(ElogE)
# 유형:
# 참고: -

# 방향성이 없는 그래프
# 1번 정점에서 N번 정점까지 최단 거리 이동 (다익스트라)
# 임의의 두 정점은 반드시 통과

import heapq
import sys
input = sys.stdin.readline

def solve(start, distance):
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for nextNode, nextCost in graph[node]:
            if distance[nextNode] > distance[node] + nextCost:
                distance[nextNode] = distance[node] + nextCost
                heapq.heappush(q, (distance[nextNode], nextNode))


if __name__ == "__main__":
    N, E = map(int ,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())


    distanceOne = [float('inf')] * (N + 1)
    solve(1, distanceOne)
    distanceV1 = [float('inf')] * (N + 1)
    solve(v1, distanceV1)
    distanceV2 = [float('inf')] * (N + 1)
    solve(v2, distanceV2)

    # 1 - v2 - v1 - N / 1 - v1 - v2 - N
    result = min(distanceOne[v2] + distanceV2[v1] + distanceV1[N], distanceOne[v1] + distanceV1[v2] + distanceV2[N])

    if result == float('inf'):
        print(-1)
    else:
        print(result)