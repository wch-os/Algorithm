# 풀이 시간 : 25분
# 시간복잡도 : O(M*a(N))
    # M : 연산 개수
    # O(a(N))
# 공간복잡도 : O(N)
# 참고 : python round() 관련 자료
#       https://blockdmask.tistory.com/418


# 0 : 합집합
# 1 : 두 원소가 같은 집합에 포함되어 있는지

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x]) # 경로 압축 최적화
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY


# m : 입력으로 주어지는 연산의 개수
N, M = map(int, input().split())

# 초기 루트 노드는 자기 자신으로 초기화
parent = [0 for _ in range(N+1)]
for i in range(N+1):
    parent[i] = i

for _ in range(M):
    op, a, b, = map(int, input().split())

    # 합집합 연산
    if op == 0:
        # 루트 노드가 다르면
        if find(a) != find(b):
            union(a, b)

    # 두 원소가 같은 집합에 포함되어 있는지
    # 즉, 같은 루트 노드를 가지고 있는지
    else:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")