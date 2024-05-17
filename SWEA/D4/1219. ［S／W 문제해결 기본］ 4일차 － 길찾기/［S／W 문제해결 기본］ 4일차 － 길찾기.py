# 풀이 시간 : 20분
# 시간복잡도 : O(0과 이어진 간선 수)
# 공간복잡도 : O(N+E)
    # 정점 수 + 간선 수
# 참고 : -

# 입력값 포맷팅을 주의해서 하자!

from collections import deque

SIZE = 100
def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        start = q.pop()

        for node in graph[start]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

    if visited[SIZE - 1]:
        return 1

    return 0


for _ in range(10):
    t, N = map(int, input().split())
    lst = list(map(int, input().split()))

    # i번째 노드와 연결되어 있는 다른 노드 데이터를 담는다.
    graph = [[] for _ in range(SIZE)]
    for i in range(0, len(lst), 2):
        graph[lst[i]].append(lst[i+1])

    visited = [False for _ in range(SIZE)] # 각 노드들 방문 처리를 위함
    print(f"#{t} {bfs(0)}")

