# 풀이 시간 : 20분
# 시간복잡도 : O(N+M)
# 공간복잡도 : O(N+M)
# 참고 : -

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(X)

    # 출발지 노드 최단 거리는 '0'이다.
    # 문제의 조건으로, 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정
    visited[X] = 0

    while q:
        start = q.popleft()

        # 인접 리스트
        for e in graph[start]:
            # 미방문 노드
            if visited[e] == -1:
                # visited 배열에, 출발지 노드에서 해당 노드까지의 최단거리 기록
                visited[e] = visited[start] + 1
                q.append(e)


# N : 도시의 개수 / M : 도로의 개수 / K : 거리 정보 / X : 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향 도로이다.

# 방문 도로 체크
visited = [-1 for _ in range(N+1)]
bfs() # 출발 노드부터, 목적지 노드까지 최단거리를 구하기 위해 bfs

result = []
for i in range(N+1):
    if visited[i] == K:
        result.append(i)

# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
if result:
    result.sort()
    for l in result:
        print(l)

# 하나도 존재하지 않으면 -1 출력
else:
    print(-1)
