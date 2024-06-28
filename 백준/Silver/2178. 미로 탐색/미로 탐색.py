# 풀이 시간: 10분
# 시간복잡도: O()
# 공간복잡도: O(NM)
# 유형: bfs
# 참고: -

# list(input())으로 받아서, 각 원소는 '1'과 '0'으로 되어있다는 것만 생각하자

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[False] * M for _ in range(N)]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, cnt = q.popleft()

        if x == N-1 and y == M-1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))



N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

print(bfs())