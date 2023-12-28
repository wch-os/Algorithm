# 풀이 시간 : 35분
# 시간복잡도 : O(N^3)
# 공간복잡도 : O(N^2)
# 참고 : -

# 생각
    # 모든 노드 쌍에 대한 최단 거리 루트에서, 첫번째 방문 지역을 알아야 된다.
    # 따라서 플로이드 알고리즘을 사용한다.
        # 이 때, graph[i][j] 값이 갱신될 때의 k를, result[i][j] = k 로 저장한다.
        
    # 예시를 의심하는데 시간을..

import sys
input = sys.stdin.readline

# N : 집하장의 개수 / M : 집하장 간 경로의 개수
N, M = map(int, input().split())

# graph[i][j] : i에서 j까지 이동하는데, 걸리는 최소 시간
graph = [[10001] * (N+1) for _ in range(N+1)]
# result[i][j] : i에서 j까지 이동하는데, 가장 먼저 거쳐야 하는 집하장 번호
result = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    # 도로는 양방향 간선
    graph[s][e] = t
    graph[e][s] = t
    # s에서 e까지 가는 데, 가장 먼저 거쳐야 하는 집하장은 e
    result[s][e] = e
    result[e][s] = s

# 시작점 정보
for i in range(1, N+1):
    graph[i][i] = 0
    result[i][i] = 0

# 플로이드 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                # k를 거칠 때 최단루트가 완성된다.
                    # k도 중간 경유지일 수 있으므로, i에서 k까지 가는 데 제일 먼저 거쳐야 하는 집하장 정보를 가져온다.
                result[i][j] = result[i][k]

# 결과 출력
for i in range(1, N + 1):
    row2 = []
    for j in range(1, N + 1):
        if result[i][j] == 0:
            result[i][j] = '-'
        row2.append(result[i][j])
    print(*row2)