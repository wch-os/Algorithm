def dfs(now, visited):
    if visited == (1<<N) - 1:
        if board[now][0]:
            dp[now][0] = board[now][0]
            return dp[now][0]

        return INF

    if dp[now][visited]:
        return dp[now][visited]

    dp[now][visited] = INF
    for i in range(N):
        if board[now][i] == 0:
            continue

        if visited & (1<<i):
            continue

        temp = dfs(i, visited | (1<<i))
        dp[now][visited] = min(dp[now][visited], temp + board[now][i])

    return dp[now][visited]



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[0] * (1<<N) for _ in range(N)]

print(dfs(0,1))