# 풀이 시간: 45분
# 시간복잡도: O(N+K)
# 공간복잡도: O(N+K)
# 유형: 위상정렬
# 참고: -

import sys
from collections import deque
input = sys.stdin.readline

# O(N + K)
def solve():
    q = deque()

    # 1. 진입차수가 0인 건물들을 queue에 넣는다.
    for i in range(1, N+1):
        if ins[i] == 0:
            result[i] = buildTimes[i] # 초기화 필요
            q.append((i, buildTimes[i]))

    # 2. 큐에서 원소를 뺀다.
    while q:
        idx, cost = q.popleft()

        # 3. 후수 건물들의 진입 차수를 빼준다.
        for next in graph[idx]:
            ins[next] -= 1

            # 후수 건물을 지을 때까지 걸리는 총 비용 = 기존 비용 vs. 선수 비용 + 후수 건물 건설 비용
            result[next] = max(result[next], cost + buildTimes[next])

            # 4. 진입 차수가 0이 된 노드를 queue에 넣어준다.
            if ins[next] == 0:
                q.append((next, result[next]))

    return result[X]


T = int(input())
for _ in range(T):
    # 건물의 개수, 건설 순서 규칙 개수
    N, K = map(int, input().split())

    # 각 건물당 건설에 걸리는 시간
    buildTimes = [0] + list(map(int, input().split()))

    ins = [0 for _ in range(N + 1)] # 건물들을 짓기 위한 진입 차수 리스트
    result = [0 for _ in range(N + 1)] # 건물들을 지을 때까지 걸리는 최소시간 리스트
    graph = [[] for _ in range(N + 1)] # 건물들 간의 연관관계를 표현하기 위한 그래프

    # 건설 순서 X, Y
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        ins[y] += 1

    X = int(input())

    print(solve())