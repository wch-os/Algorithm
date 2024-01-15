import math

def getDist(A, B):
    return math.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def dfs(now, visited):
    # 모든 정점을 방문했을 때
    if visited == (1<<N) -1:
        if graph[now][0]:
            return graph[now][0]

        return INF


    if dp[now][visited] != 0:
        return dp[now][visited]


    dp[now][visited] = INF
    for i in range(N):
        # 그러나 본 문제에서는 존재하는 모든 노드가 연결되어 있음
        # if graph[now][i] == 0:
        #     continue

        # 방문한 노드이면 pass
        if visited & (1<<i):
            continue

        temp = dfs(i, visited | (1<<i))
        dp[now][visited] = min(dp[now][visited], temp + graph[now][i])

    return dp[now][visited]



N = int(input())

dots = []
for _ in range(N):
    dot = list(map(int, input().split()))
    dots.append(dot)

graph = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        dist = getDist(dots[i], dots[j])
        graph[i][j] = dist
        graph[j][i] = dist

INF = float('inf')
dp = [[0] * (1<<N) for _ in range(N)]

print(dfs(0, 1))