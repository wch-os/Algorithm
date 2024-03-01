# 풀이 시간 : 25분 + 30분
# 시간복잡도 : O(bfs, VlogE)
# 공간복잡도 : O(N)
# 참고 : -

# 1. 나누기 / 2 가 있는 것이 아니다.
# 2-1. 순간이동의 경우를, appendleft로 가장 먼저 처리할 수 있게끔 한다.
# 2-2. -1, +1 중 -1을 우선으로 deque()에 넣어줘야 한다. (4→6)
# 3. 순간이동 인덱스 설정 수정 X
# 4. 순간이동 체크를 할 때
    # 별도의 인덱스 체크가 아니라 nx == x * 2 로 수정

from collections import deque

A, B = map(int, input().split())
q = deque()
q.append((A, 0))

visited = [False] * 100001
visited[A] = True
while q:
    x, time = q.popleft()
    if x == B:
        print(time)
        break

    # 순서가 중요!!
        # +1을 n번 하는 것보다, -1 이후에 * 2 의 경우의 수가 빠를 수 있으므로, +1 보다 우선으로 큐에 넣는다.
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True

            # 순간이동 먼저 큐에 넣도록
            if nx == x * 2:
                q.appendleft((nx, time))

            # 일반이동
            else:
                q.append((nx, time+1))