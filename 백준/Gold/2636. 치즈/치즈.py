# 풀이 시간 : 26분
# 시간복잡도 : O(4NM * time)
# 공간복잡도 : O(NM)
# 참고 : -

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def bfs():
    global flag

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    q = deque()
    q.append((0, 0))

    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    meltCnt = 0 # 이번 타임에서 녹이는 치즈 개수
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    visited[nx][ny] = True

                    # 치즈 녹이기
                    if board[nx][ny]:
                        meltCnt += 1
                        board[nx][ny] = 0
                        flag = True

                    # 공기 블록만 계속 탐색하도록 한다.
                    else:
                        q.append((nx, ny))

    return meltCnt


result = 0
meltCheeseCnt = []
for i in range(N):
    for j in range(M):
        result += 1
        flag = False

        meltCheeseCnt.append(bfs())

        # 치즈가 더 이상 안 녹았으면
        if not flag:
            print(result-1) # 1번의 무의미한 탐색이 있으므로
            print(meltCheeseCnt[-2]) # 모두 녹기 직전에 남아있는 치즈조각 개수
            exit()