# 크루스칼 알고리즘

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY


# 집의 개수, 길의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

edges = []
for _ in range(M):
    s, e, c = map(int, input().split())
    edges.append((c,s,e))

# 초기 부모 노드는 자기 자신으로 설정
parent = [0 for _ in range(N+1)]
for i in range(1, N+1):
    parent[i] = i

# 최소 간선부터 선택하기 위함
edges.sort()

result = []
for cost, start, end in edges:
    # 부모 노드가 서로 다를 시
    # 즉, 사이클을 형성하지 않을 시
    if find(start) != find(end):
        union(start, end)

        result.append(cost)
        if len(result) == N-1:
            break

# 마을 분리
print(sum(result) - max(result))