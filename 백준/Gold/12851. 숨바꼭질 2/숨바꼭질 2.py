# 풀이 시간: 25분
# 시간복잡도: O(3*(N-K))
# 공간복잡도: O(3*(N-K))
# 유형: bfs
# 참고: -

# x에서 y까지 가는 총 방법의 수를 카운트해야 하므로, visited는 사용하지 않음

from collections import deque

def bfs(x):
    # i 지점까지 가는 [가장 빠른 시간, 방법 수]
    visited = [[0, 0] for _ in range(100001)]
    visited[x] = [0, 1]

    minMove = 100000
    totalCnt = 0

    q = deque()
    q.append((x, 0))
    while q:
        x, cnt = q.popleft()

        if x == y:
            minMove = cnt
            totalCnt = visited[x][1]  # 최소 이동 횟수로, 목적지까지의 루트 개수
            break

        for k in (x - 1, x + 1, x * 2):
            # x가 범위값을 벗어나는 경우
            if k < 0 or k > 100000:
                continue

            if not visited[k][0]:  # 첫 방문일 경우
                visited[k] = [cnt + 1, visited[x][1]]
                q.append((k, cnt + 1))
            else: # 중복 방문이면서
                if visited[k][0] == cnt + 1:  # 동일한 최소 이동 횟수라면, 별도로 카운트 함
                    visited[k][1] += visited[x][1]

    return minMove, totalCnt


x, y = map(int, input().split())

m, t = bfs(x)
print(m) # 동생을 찾는 가장 빠른 시간
print(t) # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
