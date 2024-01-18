N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

def dfs(start):
    visited[start] = True

    for i in range(N):
        if not board[start][i] or visited[i]:
            continue

        dfs(i)

    result.append(start+1)


result = []
dfs(0)

print(len(result))
print(' '.join(map(str, reversed(result))))