# !. 각 건물이 완성되기까지 걸리는 최소 시간
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    q = deque()

    # 1. 진입 차수가 0인 건물들 세우기
    for i in range(1, N+1):
        if ins[i] == 0:
            q.append((i, buildTimes[i]))
            result[i] = buildTimes[i]

    while q:
        now, cost = q.popleft()

        for next in board[now]:
            # 2. 해당 건물을 진입차수로 갖는 건물들의 최소 건설 비용 계산하기
                # next 건물을 짓기 전에 지어야 할 건물들이 여러 개 있을 시
                # next 건물을 짓기까지의 총 비용 vs. now 건물을 짓기까지의 총 비용 + next 건설 비용
            result[next] = max(result[next], cost + buildTimes[next])

            # 3. 해당 건물을 진입차수로 갖는 건물들의 진입차수 -1
            ins[next] -= 1

            # 4. 진입차수가 0인 건물이 나올 시, 해당 건물을 매개로 하는 다른 건물들을 탐색할 수 있도록 queue에 삽입
            if ins[next] == 0:
                q.append((next, result[next]))



# 건물 종류 수
N = int(input())

# i번 건물을 짓기 전에 먼저 지어져야 하는 건물들의 번호를 입력받기 위한 리스트
board = [[] for _ in range(N+1)]
# 각 건물들의 진입차수 리스트
ins = [0 for _ in range(N+1)]
# 각 건물들을 건설하는데 드는 비용 리스트
buildTimes = [0 for _ in range(N+1)]
# 각 건물들을 건설하는데 드는 최소 비용 리스트
result = [0 for _ in range(N+1)]

for i in range(1, N + 1):
    lst = list(map(int, input().split()))

    buildTimes[i] = lst[0]
    for j in range(1, len(lst) - 1):
        # 선행 연관관계 체크
            # i 건물을 짓기 위해 lst[j] 건물을 지어야 함
            # 선수(lst[j]) 노드에 후수(i) 노드를 추가해야 함.
        board[lst[j]].append(i)
        ins[i] += 1 # 진입차수 체크

solve()
for i in range(1, N+1):
    print(result[i])