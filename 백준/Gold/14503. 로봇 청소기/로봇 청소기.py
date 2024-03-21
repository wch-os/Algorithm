# 풀이 시간 : 40분
# 시간복잡도 : O(NM)
# 공간복잡도 : O(NM)
# 참고 : -

# 북 서 남 동(반시계 방향) 으로 움직여야 되는데 북 동 남 서(시계 방향) 으로 움직였다.
# 동서 방향 인덱스 체크

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, idx, cnt):
    if board[x][y] == 1: # 벽
        return cnt

    # 청소할 구역이거나, 이미 청소한 구역
    else:
        board[x][y] = 2 # 청소한다.

        flag = False
        for i in range(1, 5):
            j = (idx - i) % 4 # 현재 위치에서 회전 90도 회전하기, -로 변경

            nx = x + dx[j]
            ny = y + dy[j]

            if board[nx][ny] == 0:
                flag = True
                break

        if flag: # 청소되지 않은 빈 칸이 있으면
            return dfs(nx, ny, j, cnt+1)

        else: # 후진해야 한다.
            j = (idx + 2) % 4 # 현재 위치에서 반대 방향으로
            nx = x + dx[j]
            ny = y + dy[j]

            return dfs(nx, ny, idx, cnt)



if __name__ == "__main__":
    # 북, 서, 남, 동
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    N, M = map(int, input().split())

    # 로봇 청소기 (x, y) 좌표, 바라보는 방향
    r, c, d = map(int, input().split())

    # 0: 청소되지 않은 빈 칸, 1: 벽
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    print(dfs(r, c, d, 1))