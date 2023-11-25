# 육각형이므로, 6개의 지역에 접근해야 한다.
# 닫힌 구역을 어떻게 판단하지?

# 풀이 시간 : 1시간 30분 + 1시간
# 시간복잡도 : O(ne)
    # n : 정점 개수, 여기서는 빈 공간의 개수
    # e : 간선 개수, 각 정점마다 6개의 간선
# 공간복잡도 : O((W+1) * (H+1))
# 참고 : https://reliablecho-programming.tistory.com/110


import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # row가 짝수일 때
    dx = [0, 0, -1, -1, 1, 1]
    dy = [1, -1, 0, 1, 0, 1]

    # row가 홀수일 때
    dy2 = [1, -1, -1, 0, -1, 0]

    queue = deque()
    queue.append((0, 0))

    visited = [[False] * (W + 2) for _ in range(H + 2)]
    visited[0][0] = True

    light = 0
    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            if x % 2 == 1:
                ny = y + dy[i]
            else:
                ny = y + dy2[i]

            # 정상 인덱스 & 미방문 노드일 경우
            if 0 <= nx < H+2 and 0 <= ny < W+2:
                # 건물일 시 count
                if board[nx][ny] == 1:
                    light += 1

                # 빈 공간 & 미방문 노드일 시, 큐에 append
                elif board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return light



W, H = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(H)]

# 상하좌우 외곽 데이터에 공백을 넣어두자
    # 외곽에 있는 '빈 공간'을 중심으로, 건물들과 인접한 경우를 count하면 문제에서 원하는 답 출력
board = [[0] * (W+2) for _ in range(H+2)]
for i in range(H):
    for j in range(W):
        board[i+1][j+1] = data[i][j]

print(bfs())