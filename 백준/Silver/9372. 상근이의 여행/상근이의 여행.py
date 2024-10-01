import sys
from collections import deque
input = sys.stdin.readline


def solve():
    visited = [True] + [False] * N

    q = deque([1])
    visited[1] = True
    
    result = 0
    while q:
        now = q.popleft()
        
        if not visited[now]:
            visited[now] = True
            result += 1

        if all(visited):
            return result

        for next in graph[now]:
            q.append(next)


T = int(input()) # 테스트케이스의 수
for _ in range(T):

    N, M = map(int, input().split()) # 국가의 수, 비행기의 종류
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(solve())
