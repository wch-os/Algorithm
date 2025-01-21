# 풀이 시간: 1시간
# 시간복잡도: O(N^2 * logN)
# 공간복잡도: O(N^2)
# 유형: bfs, priority queue
# 참고:
    # 질문 게시판
    # - 초기 상어 위치, 지나다닐 수 있게 0 초기화
    # - '(1, 0) / (0, 3) 물고기 중 어떤 것을 먼저 먹어야 하는가?' 를 생각해보자. → priority queue 사용이 편리함
    # 0 9 0 1
    # 1 0 0 0
# 생각:
    # 오랜만에 알고리즘 푸니 재밌다.
    # 구현 문제답게 문제의 흐름을 빠르고 정확히 파악하고, 글로 정리하면서 푸는 것을 추천한다. (상어 초기화와 계속 ↑, ←, →, ↓ 탐색으로 생각하다가.. ㅠ)
    # 파이썬으로 객체 타입으로 쓰려니 어색하다..
    # 자바로 풀다가 파이썬으로 넘어왔는데 객체 지향적으로 풀기에는 역시 자바가..



import heapq
import sys
from collections import deque
input = sys.stdin.readline

class Shark:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y

"""상어가 어디에 위치한 물고기를 먹기 위해 이동하는지 계산하는 함수"""
def fishToShark(shark):
    # bfs
    visited = [[0] * N for _ in range(N)]

    pq = []

    q = deque()
    q.append((shark.x, shark.y, 0))
    visited[shark.x][shark.y] = True

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while q:
        x, y, dis = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미방문 지역 & 이동 가능
            if (0 <= nx < N and 0 <= ny < N) and not visited[nx][ny] and board[nx][ny] <= shark.size:
                # 먹을 수 있음
                if 0 < board[nx][ny] < shark.size:
                    heapq.heappush(pq, (dis + 1, nx, ny))

                # 이동만 가능
                visited[nx][ny] = True
                q.append((nx, ny, dis + 1))

    return heapq.heappop(pq) if pq else None


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0 # 몇 초 동안 도움을 요청하지 않고, 물고기를 먹을 수 있는지

# 1. 상어 위치 파악 (size, x, y)
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = Shark(size=2, x=i, y=j)
            """0으로 초기화해야 지나다닐 수 있다..."""
            board[i][j] = 0

# 2. 먹을 수 있는 물고기를 구한다
eatFish = 0
while True:
    # eatFishX, eatFishY, distance
    fishData = fishToShark(shark)

    if fishData is None:
        break
    else:
        # 상어 이동해서 물고기 먹음
        shark.x = fishData[1]
        shark.y = fishData[2]
        result += fishData[0]  # 이동 시간
        board[shark.x][shark.y] = 0

    eatFish += 1
    if eatFish == shark.size:
        shark.size += 1
        eatFish = 0

print(result)