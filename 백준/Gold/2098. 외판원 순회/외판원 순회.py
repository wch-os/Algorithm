# 풀이 시간 : N시간
# 시간복잡도 : O(N * 2^N * N)
# 공간복잡도 : O(N * 2^N)
# 참고 : https://withhamit.tistory.com/246 (이론)
#       https://velog.io/@dltmdrl1244/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8CTSP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 → dp 배열을 INF로 초기화한 코드 (틀림)
#       https://velog.io/@jxlhe46/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-%EB%AC%B8%EC%A0%9C → 올바르게 푼 코드 (맞음)
#       https://programmer-hoo.tistory.com/59 → 55% 시간초과 해결

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')

# dp[i][visited] : dp[현재 노드][지금까지 방문한 노드] = 나머지 정점을 이동하고 출발 정점으로 돌아오는데 걸리는 최소 비용
dp = [[0] * (1<<N) for _ in range(N)]


def dfs(now, visited):
    # 모든 노드를 방문했을 시
    if visited == (1<<N)-1:
        if graph[now][start]: # 시작점까지 가는 경로
            return graph[now][start]

        return INF # 없으면 INF 값 반환


    # 중복 경로일 시 이전 구한 값 return
    if dp[now][visited] != 0:
        return dp[now][visited]


    # 노드 방문
    dp[now][visited] = INF # 방문 표시, 길이 없어도 "if dp[now][visited] != 0"이 무한 재귀가 되지 않도록
    for i in range(0, N):
        if graph[now][i] == 0:
            continue

        # i가 이전에 방문한 노드인지 판단 ("&")
        if visited & (1<<i):
            continue

        # i 노드를 방문한다. ("|")
        # 그리고, 방문하지 않은 노드들을 방문했을 때 걸리는 최소 비용을 temp에 저장한다.
        temp = dfs(i, visited | (1<<i))

        # 현재 노드에서 i까지 비용 + temp 와 비교한다.
        dp[now][visited] = min(dp[now][visited], graph[now][i] + temp)

    return dp[now][visited]


start = 0
bit = 1
print(dfs(start, bit))
