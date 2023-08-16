import sys
input = sys.stdin.readline
INF = float("inf") - 10001

N, M = map(int, input().split()) #도시의 개수, 버스의 개수
minDis = [INF] * (N+1) #도착지까지의 최소 거리
graph = [] #(출발지, 목적지, 비용) 담는 자료구조

def bellman(start):
    minDis[start] = 0 #출발지까지의 거리는 0

    #노드의 개수가 N개, 양의 가중치만 갖는 그래프라면 1번만으로 모든 간선의 최소 거리를 알 수 있다.
    #음의 가중치가 있는 그래프라면, 가중치가 갱신될 수 있으므로 추가적으로 반복을 해주어야 한다.
    for i in range(N):
        # 그래프의 모든 간선을 갱신한다.
        for s, e, c in graph:
            if minDis[e] > minDis[s] + c:
                minDis[e] = minDis[s] + c

                #음의 순환 존재
                if i == N - 1:
                    return True
    return False

for i in range(M):
    s, e, c = map(int, input().split())
    graph.append((s, e, c))

minus_cycle = bellman(1)

#음의 순환이 존재하면 "-1"
if minus_cycle:
    print("-1")

#음의 순환이 존재하지 않은 그래프라면
else:
    for i in range(2, N+1):
        # 해당 노드까지 가는 경로 없으면
        if minDis[i] == INF:
            print(-1)
        # 각 노드까지의 최소 거리 출력
        else:
            print(minDis[i])