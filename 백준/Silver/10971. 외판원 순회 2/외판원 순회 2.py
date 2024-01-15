# 2098번을 풀면서, 다시 제출해보는 외판원 문제
# 저번 제출 코드를 리뷰하면서 최적화
    # https://www.acmicpc.net/source/66806749

# 외판원 순회
# 어느 지점에서 시작해도 어차피 같은 경로의 최적 경로가 산출된다.

# 백트래킹
# 길이 없으면 break
# 다시 시작 지점으로 돌아오면 break

# 메모제이션
# 특정 노드를 방문하게 되는 경우의 수는 매우 많다.
# 중복 경로에 대한 메모제이션 필요
    # i : 현재 방문 노드 / j : 지금까지 방문한 노드 (bit)
    # dp[i][visited] = i에서 미방문 노드에 대한 경로 cost 계산
                     # 이 때, 출발 노드까지 가는 비용은 각각이므로 별도의 계산 필요 (이것은 dp값에 저장 X)

    # dp[i][visited] = min(dp[i][visited], dp[j][vistied | (1 << j)] + graph[i][j])


def dfs(go, cost, depth):
    global result

    # 모든 노드를 방문했을 시
    if depth == N:
        # 마지막 노드에서 출발점으로 되돌아 올 수 있을 때
        if graph[go][0]:
            result = min(result, cost + graph[go][0])
        return

    elif result < cost:
        return

    for i in range(N):
        if not visited[i] and graph[go][i] != 0:
            visited[i] = True
            dfs(i, cost + graph[go][i], depth + 1)
            visited[i] = False


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

result = float('inf')

# 출발점은 '0'
# 출발점과 연결되지 않는 길은 가지 않는다.
visited[0] = True
for i in range(N):
    if graph[0][i]:
        visited[i] = True
        dfs(i, graph[0][i], 2)  # 0과 i를 방문하므로 depth는 2
        visited[i] = False

print(result)