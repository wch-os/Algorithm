# 풀이 시간 : 20분
# 시간복잡도 : O(bfs)
# 공간복잡도 : O(100000)
# 참고 : https://www.acmicpc.net/board/view/68596

# visited[i] = min(visited[i-1], visited[i+1], visited[i/2])
# → bfs로 도달하는 것이 더 빠르겠다.

# 이동 규칙이 대칭이 아니다..
# 범위 체크하고 방문 체크

from collections import deque

a, b = map(int, input().split())

q = deque()
q.append(a)
visited = [0] * 100001

while q:
    a = q.popleft()

    if a == b:
        print(visited[a])
        break

    for i in (a + 1, a - 1, a * 2):
        # visited 값 | 범위 바깥일 경우
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = visited[a] + 1
            q.append(i)