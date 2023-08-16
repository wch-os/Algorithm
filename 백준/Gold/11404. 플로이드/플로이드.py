import sys
input = sys.stdin.readline
INF = float('inf')

graph = []
minDis = []

N = int(input()) #도시의 개수
M = int(input()) #버스의 개수

#자기 자신의 도착 지점은 0, 나머지는 INF로 초기화
minDis = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i!=j:
            minDis[i][j] = INF

#그래프 간선 그리기
for _ in range(M):
    s, e, c = map(int, input().split())
    minDis[s][e] = min(minDis[s][e], c)

#플로이드 알고리즘
#k를 경유하는 경우와 비교해, 최소 비용 갱신
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            minDis[i][j] = min(minDis[i][j], minDis[i][k] + minDis[k][j])

#모든 지점에서 모든 지점까지의 최소 비용 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        if minDis[i][j] == INF:
            print(0, end=" ")
        else:
            print(minDis[i][j], end= " ")
    print()