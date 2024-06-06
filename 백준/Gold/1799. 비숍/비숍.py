# 풀이 시간: 2시간 30분
# 시간복잡도: O(2^(N*N/4))
    # N*N의 크기를 검정/흰 (N/2)*(N/2) * 2의 크기로 생각해서 풀이
# 공간복잡도: O(N^2)
# 유형: backtracking
# 참고: https://suri78.tistory.com/184
    # https://ji-gwang.tistory.com/481

import sys
input =sys.stdin.readline

def dfs(row, col, cnt):
    global result

    # 2칸씩 널뛰기 하며 그림 그려보면 쉽게 이해 가능
    if N % 2: # 홀수
        if col == N:
            row += 1
            col = 0
        elif col == N + 1:
            row += 1
            col = 1
    else: # 짝수
        if col == N:
            row += 1
            col = 1
        elif col == N + 1:
            row += 1
            col = 0

    # 마지막 행
    if row == N:
        result = max(result, cnt)
        return

    # 양대각선 좌표를 최상단으로 올린다.
    if board[row][col] == 1 and not visited[0][row + col] and not visited[1][row - col]:
        visited[0][row + col] = True 
        visited[1][row - col] = True
        dfs(row, col + 2, cnt + 1)
        visited[0][row + col] = False
        visited[1][row - col] = False

    dfs(row, col + 2, cnt)



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 양대각선 좌표를 최상단으로 올릴 때, 최대 범위가 2N이다.
visited = [[False] * (N * 2) for _ in range(2)]

# 검은색 칸
result = 0
dfs(0, 0, 0)
blackCnt = result

# 흰색 칸
result = 0
dfs(0, 1, 0)
whiteCnt = result

print(blackCnt + whiteCnt)