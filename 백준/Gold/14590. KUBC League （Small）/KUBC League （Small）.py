def dfs(now, visited):
    # 메모제이션 한 값이 있을 때
    if dp[now][visited] != -1:
        return dp[now][visited]

    # dp 배열을 -1로 초기화 후 0 할당
    dp[now][visited] = 0
    for i in range(N):
        # 이미 방문한 노드일 경우
        if visited & (1 << i):
            continue

        # 현재 노드에서 다음 노드 갈 경로가 없으면
            # 이 문제에서는 now번이 i번을 이길 수 없으면
        if board[now][i] == 0:
            continue

        # i번을 이길 수 있으면
            # i가 이기는 상대를 꼬리를 물며 찾는다.
        temp = dfs(i, visited | (1 << i))

        ## 최소 비용이 아닌 최대 길이를 저장
        dp[now][visited] = max(dp[now][visited], board[now][i] + temp)

    return dp[now][visited]


def trace(now, visited):
    for i in range(N):
        if board[now][i] == 0:
            continue

        if visited & (1 << i):
            continue

        # "현재 노드에서 미방문 노드를 방문했을 때 최소 비용"과
            # "i 노드에서 미방문 노드를 방문했을 때 최소 비용"이 같아야 한다.
        ## now가 i 직전에 방문했다는 의미이다. ##
        if dp[now][visited] == dp[i][visited | (1 << i)] + 1:
            tails.append(i+1)
            trace(i, visited | (1 << i))
            break


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 최소 비용을 저장하는 것과는 다르다.
# 현재 i번째 노드에서, visited 방문한 상태일 때 최대 길이를 저장한다.
dp = [[-1] * (1<<N) for _ in range(N)]

tails = [1]
INF = float('inf')

# dfs를 마치면 0번 선수(태양)를 기준으로, 꼬리를 무는 사람이 몇 명인지 구할 수 있다.
# dp 값에는 0번 선수(태양)에서 꼬리 끝까지 최소 경로 비용이 나오지만, 경로 순서를 찾는 문제이므로 의미가 없다.
dfs(0, 1)

# 방문한 노드인지 역추적한다.
trace(0, 1)

print(len(tails))
print(*tails)