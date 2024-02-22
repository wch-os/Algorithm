# 풀이 시간 : 20분
# 시간복잡도 : O(bfs)
# 공간복잡도 : O(100000)
# 참고 : https://www.acmicpc.net/board/view/68596

# visited[i] = min(visited[i-1], visited[i+1], visited[i/2])
# → bfs로 도달하는 것이 더 빠르겠다.

# 이동 규칙이 대칭이 아니다..

from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 0))
visited = [0] * 100001

while q:
    a, time = q.popleft()

    if a == b:
        print(time)
        exit()

    # visited 값 | 범위 바깥일 경우
    if a < 0 or 100000 < a or visited[a]:
        continue

    visited[a] = time

    q.append((a+1, time+1))
    q.append((a-1, time+1))
    q.append((a*2, time+1))