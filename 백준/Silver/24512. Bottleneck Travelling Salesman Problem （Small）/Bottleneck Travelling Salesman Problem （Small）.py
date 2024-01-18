def dfs(now, starting, depth, cost):
    global minCost

    if depth == N:
        if board[now][starting]:
            cost = max(cost, board[now][starting])
                
            if minCost > cost:
                minCost = cost

                result.clear()
                for t in tail:
                    result.append(t)


    for k in range(N):
        if not visited[k] and board[now][k]:
            visited[k] = True
            tail.append(k+1)

            dfs(k, starting, depth+1, max(cost, board[now][k]))

            visited[k] = False
            tail.pop()



N, M = map(int, input().split())
board = [[0] * (1<<N) for _ in range(N)]

for _ in range(M):
    s, e, c = map(int, input().split())
    board[s-1][e-1] = c

INF = float('inf')
minCost = INF
result = []

for i in range(2):
    tail = [i+1]
    visited = [False] * N
    visited[i] = True

    dfs(i, i, 1, 0)


if minCost == INF:
    print(-1)
else:
    print(minCost)
    print(*result)