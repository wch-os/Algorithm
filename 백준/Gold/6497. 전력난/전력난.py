# 풀이 시간: 25분
# 시간복잡도: O(n * logn | n * a(m))
# 공간복잡도: O(n | m)
# 유형: mst, union-find
# 참고: -

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    parent[rootX] = rootY

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x]) # union 되었을 때, 부모 노드를 갱신할 수 있도록
    return parent[x]
    


while True:
    m, n = map(int, input().split()) # 집의 수, 길의 수
    if m == 0 and n == 0:
        break
    roads = [list(map(int, input().split())) for _ in range(n)] # x번 집과 y번 집 사이에 거리가 z인 양방향 도로

    # 거리 기준으로 오름차순 정렬 (kruskal)
    roads.sort(key=lambda x: x[2])

    # 자기 자신을 루트 노드로 지정
    parent = [0] * m
    for i in range(m):
        parent[i] = i

    # 절약할 수 있는 비용
    result = 0
    for x, y, z in roads:
        if find(x) != find(y):
            union(x, y)

        # 사이클이 형성되는 경우, 절약 가능하다.
        else:
            result += z

    print(result)