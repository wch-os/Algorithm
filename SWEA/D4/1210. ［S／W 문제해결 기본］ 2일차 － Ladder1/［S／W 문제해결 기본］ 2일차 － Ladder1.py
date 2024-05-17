# 풀이 시간 : 27분
# 시간복잡도 : O(최종경로길이)
# 공간복잡도 : O(N^2)
# 참고 : -


SIZE = 100

def dfs(x, y):
    if x == 0:
        return y

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < SIZE and 0 <= ny < SIZE and board[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                return dfs(nx, ny)


# 좌 우 상
dx = [0, 0, -1]
dy = [-1, 1, 0]

for _ in range(10):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(SIZE-1)]
    endLine = list(map(int, input().split()))
    board.append(endLine)

    endY = 0
    for i in range(len(endLine)):
        if endLine[i] == 2:
            endY = i


    visited = [[False] * SIZE for _ in range(SIZE)]
    print(f"#{t} {dfs(SIZE-1, endY)}")
