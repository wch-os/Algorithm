# 풀이 시간 : 17분
# 시간복잡도 : O(a(N)))
    # 경로 압축한 find()의 시간복잡도
    # 경로 압축하지 않았을 때는 트리의 높이 O(h)
        # 최악의 경우, 즉 하나의 체인 형태일 경우 O(N)이다.
# 공간복잡도 : O(N)
# 참고 : -

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x, y):
    findX = find(x)
    findY = find(y)

    if ranks[findY] < ranks[findX]:
        parents[findY] = findX
        ranks[findX] += ranks[findY]
    else:
        parents[findX] = findY
        ranks[findY] += ranks[findX]

# O(a(N))
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


N, Q = map(int, input().split())

lst = []
for _ in range(Q):
    s, e, c, t = map(int, input().split())
    lst.append((c, t, s-1, e-1)) # 건설 비용을 최소, 빠르게



parents = [i for i in range(N)]
ranks = [1 for i in range(N)]


result = 0
lst.sort()
totalCost, totalTime, roadCnt = 0, 0, 0
for cost, time, start, end in lst:
    if find(start) != find(end):
        union(start, end)

        roadCnt += 1
        totalCost += cost
        totalTime = max(totalTime, time)

if roadCnt == N-1:
    print(totalTime, totalCost)
else:
    print(-1)