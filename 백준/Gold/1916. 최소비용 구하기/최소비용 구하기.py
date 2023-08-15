import heapq
import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input()) #도시의 개수
M = int(input()) #버스의 개수

graph = [[] for _ in range(N+1)]

#출발지, 목적지, 비용 입력
for _ in range(M):
    values = input().split()

    start = int(values[0])
    end = int(values[1])
    distance = int(values[2])

    graph[start].append((end, distance))


result = [INF for _ in range(N+1)] #각 도시까지 가는 겨올 MAX로 초기화
wantS, wantE = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #해당 노드까지의 거리, 시작노드
    #result[start] = 0

    while q:
        dis, node = heapq.heappop(q)

        if result[node] < dis: #지금 저장되어 있는 최소거리보다 길다면, 예전 원소이므로 무시
            continue

        for next in graph[node]: #해당 노드와 인접 노드 탐색
            cost = dis + next[1] #지금까지의 거리 + 인접 노드까지의 거리
            if result[next[0]] > cost: #인접 노드까지의 거리 갱신
                result[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(wantS)
print(result[wantE]) #목적지까지의 최소 cost 구하기