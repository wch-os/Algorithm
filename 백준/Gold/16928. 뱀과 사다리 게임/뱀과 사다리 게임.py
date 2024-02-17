# 풀이 시간 : 28분 + 30분
# 시간복잡도 : O(bfs)
# 공간복잡도 : O(1)
# 참고 : https://www.acmicpc.net/board/view/119158 (반례)

# 사다리는 타고, 뱀은 피해야한다.
    # 뱀 또한 이용..
# 6칸 범위 내에 사다리가 있으면 사다리를 탄다
# 방문 체크를 안 함

import sys
from collections import deque
input = sys.stdin.readline

# 사다리 수, 뱀 수
N, M = map(int, map(int, input().split()))

road = []
visited = [0] * 106
for _ in range(N+M):
    s, e = map(int, map(int, input().split()))
    road.append((s, e))

q = deque()
q.append(1)

while q:
    x = q.popleft()

    if x == 100:
        print(visited[100])
        exit()

    for i in range(1, 7):
        nx = x + i

        # 사다리나 뱀일 경우, 이용한다.
        for s, e in road:
            if nx == s:
                nx = e

        # 중복 방문 X
        if not visited[nx]:
            visited[nx] = visited[x] + 1
            q.append(nx)