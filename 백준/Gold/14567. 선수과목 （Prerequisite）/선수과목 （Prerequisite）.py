# 풀이 시간: 17분 + 8분 + 20분
# 시간복잡도: O(N+M)
# 공간복잡도: O(N)
# 유형: bfs, 위상정렬(topological sort)
# 참고:
    # 위상정렬 개념
    # https://velog.io/@kimdukbae/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-Topological-Sorting
    # https://m.blog.naver.com/ndb796/221236874984

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    # 1. 진입 차수가 0인 모든 노드를 queue에 넣는다.
    for i in range(1, N + 1):
        if not ins[i]:
            q.append((i, 1))

    # 2. 큐에서 원소를 꺼낸다.
    while q:
        x, cost = q.popleft()

        # !. 해당 과목을 수강하는데 최소 비용을 저장한다.
        result[x] = cost

        for next in graph[x]:

            # 3. 진입 차수를 하나 빼준다.
            ins[next] -= 1

            # 4. 진입 차수가 0이 된 노드를 queue에 넣는다.
            if not ins[next]:
                q.append((next, cost + 1))



N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

q = deque()
ins = [0] * (N+1)
result = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    ins[b] += 1 # b의 진입차수 + 1

solve()
print(*result[1:])