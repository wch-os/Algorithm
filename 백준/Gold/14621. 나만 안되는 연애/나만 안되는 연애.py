# 풀이 시간 : 40분
# 시간복잡도 : O(a(N))
# 공간복잡도 : O(N)
# 참고 : -

# 처음에 다익스트라/플로이드로 생각했다가, 그래프가 아닌 트리 형식이라 MST로 접근해서 풀었다.
# 열흘 전에 풀었던 union-find 문제처럼 "집합의 크기"를 기준으로 효율적인 union을 하고자 했다.


import sys
input = sys.stdin.readline

# O(2*find())
def union(x, y):
    findX = find(x)
    findY = find(y)

    if ranks[findX] > ranks[findY]: # findX 크기가 더 큰 경우, findX
        parents[findY] = findX
        ranks[findX] += ranks[findY]
    else:
        parents[findX] = findY
        ranks[findY] += ranks[findX]

# O(a(N))
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x]) # 경로 최적화
    return parents[x]



N, M = map(int, input().split())
uni = list(input().split())

lst = []
parents = [i for i in range(N)]  # 자기 자신 부
ranks = [1 for i in range(N)]

for _ in range(M):
    s, e, dis = map(int, input().split())
    s, e = s - 1, e - 1

    if uni[s] != uni[e]:  # 다른 색깔이면 유효한 경로이다.
        lst.append((dis, s, e))

totalDis, cnt = 0, 0
lst.sort()  # 거리가 짧은 경로부터 탐색하기 위함
for (dis, s, e) in lst:
    if find(s) != find(e):
        union(s, e)
        totalDis += dis
        cnt += 1

if cnt == N-1:
    print(totalDis)
else:
    print(-1)