# 풀이 시간 : 25분 + 30분
# 시간복잡도 : O(MlogM)
# 공간복잡도 : O(M)
# 참고 : -

# 프림, 크루스칼 알고리즘
# 빠른 입출력

# 프림 알고리즘을 잘못 알고 있었다..
    # False : 모든 간선들 중 최소 간선을 찾아 이동
    # True : 방문한 노드의 미방문 노드 간선들 중 최소 간선을 찾아 이동

# 왜 pop()을 하고 다시 미방문 체크를 해줘야 하지??

import heapq
import sys
input = sys.stdin.readline

def prim():
    pq = [] # 간선(거리, 시작 노드) 저장
    heapq.heappush(pq, (0, 1))

    costList = []
    while pq:
        # 연결된 간선들 중 최소 간선을 pop한다.
        cost, now = heapq.heappop(pq)

        if not visited[now]:
            visited[now] = True
            costList.append(cost)

            if len(costList) == N:
                break
            for dist, end in graph[now]:
                if not visited[end]:
                    # 연결된 간선들 중 미방문 노드 간선을 모두 heap에 넣는다.
                    heapq.heappush(pq, (dist, end))

    return sum(costList) - max(costList)



# 집의 개수, 길의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))
    graph[e].append((c, s))

print(prim())
