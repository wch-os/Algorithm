# 풀이 시간 : 1시간 30분
# 시간복잡도 : O(NM * (dfs + ㅜ))
# 공간복잡도 : O(NM)
# 참고 : -

# dfs 탐색할 때마다 visited 초기화

import sys
input = sys.stdin.readline

def dfs(x, y, cnt, score):
    global result

    if cnt == 4:
        scores.append(score)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N and 0 <= ny < M) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, score + board[nx][ny])
            visited[nx][ny] = False


def straight(x, y, cnt, score, line):
    if cnt == 3:
        if line == da:
            if 0 <= x - 1 < N and 0 <= y - 1 < M:
                scores.append(score + board[x-1][y-1])
            if 0 <= x + 1 < N and 0 <= y - 1 < M:
                scores.append(score + board[x+1][y-1])

        else:
            if 0 <= x - 1 < N and 0 <= y - 1 < M:
                scores.append(score + board[x-1][y-1])
            if 0 <= x - 1 < N and 0 <= y + 1 < M:
                scores.append(score + board[x-1][y+1])
        return

    nx = x + line[0]
    ny = y + line[1]

    if 0 <= nx < N and 0 <= ny < M:
        straight(nx, ny, cnt + 1, score + board[nx][ny], line)



if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    scores = []

    da = [0, 1]
    db = [1, 0]

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            straight(i, j, 1, board[i][j], da)
            straight(i, j, 1, board[i][j], db)
            visited[i][j] = False

    result = max(scores)
    print(result)