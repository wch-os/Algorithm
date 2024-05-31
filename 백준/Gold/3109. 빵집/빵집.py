# 풀이 시간: 20분 + 20분
# 시간복잡도: O(R*C*3)
# 공간복잡도: O(RC)
# 유형: dfs
# 참고:

R, C = 0, 0
dx = [-1, 0, 1]
dy = [1, 1, 1]
def dfs(x, y):
    global result

    if y == C - 1:
        result += 1
        return True # root를 찾았을 경우

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < R and 0 <= ny < C) and (board[nx][ny] == ".") and (not visited[nx][ny]):
            visited[nx][ny] = True

            if dfs(nx, ny): # 해당 dfs 탐색에서 root를 찾았으면, 더 이상의 탐색은 필요가 없다.
                return True

            # root를 찾지 못했을 경우, 나머지 탐색을 진행한다.


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

result = 0
for i in range(R):
    visited[i][0] = True
    dfs(i, 0)

print(result)