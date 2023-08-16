import sys
input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split()) #도시의 개수, 버스의 개수
minDis = [INF] * (N+1)
graph = []

def bellman(start):
    minDis[start] = 0

    for i in range(N):
        for s, e, c in graph:
            if minDis[s] != INF and minDis[e] > minDis[s] + c:
                minDis[e] = minDis[s] + c
                if i == N - 1:
                    return True

    return False

for i in range(M):
    s, e, c = map(int, input().split())
    graph.append((s, e, c))

minus_cycle = bellman(1)

if minus_cycle:
    print("-1")

else:
    for i in range(2, N+1):
        if minDis[i] == INF:
            print(-1)
        else:
            print(minDis[i])