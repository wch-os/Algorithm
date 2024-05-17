# 풀이 시간 : 15분
# 시간복잡도 : O(a(N))
# 공간복잡도 : O(N)
# 참고 : -

import sys
input = sys.stdin.readline

def union(x, y):
    findX = find(x)
    findY = find(y)

    if findX != findY:
        if ranks[findX] > ranks[findY]:
            ranks[findX] += ranks[findY]
            parents[findY] = findX
        else:
            ranks[findY] += ranks[findX]
            parents[findX] = findY


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]



V, E = map(int, input().split())

costSorted = []
for _ in range(E):
    start, end, cost = map(int, input().split())
    costSorted.append((cost, start-1, end-1))

parents = [i for i in range(V)] # 부모 노드 초기화
ranks = [1 for i in range(V)] # 해당 분리집합 크기

result = 0
costSorted.sort() # 비용이 작은 노드부터 union
for c, s, e in costSorted:
    if find(s) != find(e):
        union(s, e)
        result += c

print(result)