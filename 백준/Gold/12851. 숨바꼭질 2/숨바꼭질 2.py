# 풀이 시간: 25분 + 1시간
# 시간복잡도: O(3*(N-K))
# 공간복잡도: O(3*(N-K))
# 유형: bfs
# 참고: -

# 가장 빠르게 이동하는 노드들을 큐에 넣어서 "x = y" 일 경우를 모두 찾는 방법과
# 가장 빠르게 이동하면서 중복 방문하는 횟수를 따로 저장해서 "x = y"일 때 바로 return 되는 두 가지 방법으로 풀 수 있을 듯하다.

from collections import deque

def bfs(x):
    # i 지점까지 가는 [가장 빠른 시간, 방법]
    visited = [[0, 0] for _ in range(100001)]
    visited[x] = [0, 1]

    q = deque()
    q.append(x)
    while q:
        x = q.popleft()

        if x == y:
            break

        for nx in (x - 1, x + 1, x * 2):
            # x가 범위값을 벗어나는 경우
            if nx < 0 or nx > 100000:
                continue

            # 첫 방문일 때, 시간 및 방법 추가
            if not visited[nx][0]:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] += visited[x][1]
                q.append(nx)

            # 최소 이동으로 중복 방문일 경우, 방법 추가
            elif visited[nx][0] == visited[x][0] + 1:
                visited[nx][1] += visited[x][1]


    return visited[x][0], visited[x][1]


x, y = map(int, input().split())

m, t = bfs(x)
print(m) # 동생을 찾는 가장 빠른 시간
print(t) # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
