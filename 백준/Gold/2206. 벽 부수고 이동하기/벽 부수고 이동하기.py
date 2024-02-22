# 풀이 시간 : 1시간 + 30분
# 시간복잡도 : O(2N^2)
# 공간복잡도 : O(2N^2)
# 참고 : -
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, False))
    visited[0][0][0] = 1
    visited[0][0][1] = 1

    while q:
        x, y, item = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                ex = board[nx][ny]
                # (nx, ny) 벽
                if  ex == "1":
                    # 지금까지 item 미사용 & 해당 칸 벽 미방문
                    if not item and not visited[nx][ny][1]:
                        visited[nx][ny][1] = visited[x][y][0] + 1 # 해당 칸 벽 뚫는다고 체크
                        q.append((nx, ny, True))

                # (nx, ny) 길
                else:
                    # 지금까지 item 사용 & 해당 칸 길 미방문
                        # 길인데 item 사용한 경우에는, visited[nx][ny][1] 방문 여부를 체크해줘야
                    if item and not visited[nx][ny][1]:
                        q.append((nx, ny, True))
                        visited[nx][ny][1] = visited[x][y][1] + 1

                    # 지금까지 item 미사용 & 해당 칸 벽 미방문
                        # 길인데 item 미사용한 경우에는, visited[nx][ny][0] 방문 여부를 체크해줘야
                    elif not item and not visited[nx][ny][0]:
                        q.append((nx, ny, False))
                        visited[nx][ny][0] = visited[x][y][0] + 1



N, M = map(int, input().split())
board = [input() for _ in range(N)]

visited = [[[0 for _ in range(2)] for _ in range(M)]  for _ in range(N)]
visited[0][0][0] = 1

dx = [-1,0,0,1]
dy = [0,-1,1,0]

bfs()

# 아이템 사용, 미사용
itemNo = visited[N - 1][M - 1][0]
itemYes = visited[N - 1][M - 1][1]

# 탈출 불가능
if itemNo == 0 and itemYes == 0:
    print(-1)
# 아이템을 써도, 안써도 탈출 가능할 때
elif itemNo and itemYes:
    print(min(itemNo, itemYes))
# 둘 다 값이 있을 때
else:
    print(max(itemNo, itemYes))