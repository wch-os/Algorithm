# https://www.acmicpc.net/board/view/125351
# 이전 코드가 틀린 이유 : 마지막 지점에서, 첫번째 지점으로 가는 경로를 고려하지 않았다..

# i : i도시 | idx : 방문한 도시의 개수 | cost : 지금까지 든 비용 | start : 시작지점
def dfs(i, idx, cost, start):
    global result

    # 출발지 제외하고, 모든 도시를 방문했을 경우
    if idx == N-1:
        # 마지막 지점에서, 첫번째 지점으로 가는 경로가 존재해야 한다!
        if W[i][start]:
            cost += W[i][start]
            result = min(result, cost)
        return

    # 백트래킹 시간 절약을 위해.. cost보다 큰 경우 바로 return 해준다.
    elif result < cost:
        return

    for j in range(N):
        # j는 출발점이어서는 안된다.
        # j 도시가 미방문 도시였을 경우 & i에서 j까지 가는 경로가 있는경우
        if j != start and visited[j] == False and W[i][j] > 0:
            visited[j] = True
            dfs(j, idx + 1, cost + W[i][j], start)
            visited[j] = False


N = int(input()) # 도시의 수
W = [list(map(int, input().split())) for _ in range(N)] # 비용 행렬

visited = [False] * N # 각 도시 방문 여부

idx = 0
cost = 0

result = float('INF')

for i in range(N):
    #visited[i] = True
    dfs(i, idx, cost, i)
    #visited[i] = False

print(result)