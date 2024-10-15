# 풀이 시간: 15분
# 시간복잡도: O(N+M)
# 공간복잡도: O(N+M)
# 유형: 위상정렬
# 참고: -

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    q = deque()

    # 진입차수가 0인 노드
    for i in range(1, N+1):
        if ins[i] == 0:
            q.append(i)

    result = []
    while q:
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            ins[next] -= 1
            if ins[next] == 0:
                q.append(next)

    print(*result)



N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
ins = [0] * (N+1) # 진입차수

for i in range(M):
    a, b = map(int, input().split())
    ins[b] += 1
    graph[a].append(b)

solve()