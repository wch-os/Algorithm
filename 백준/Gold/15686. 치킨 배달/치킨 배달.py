import sys
input = sys.stdin.readline

# N*N 도시, M개의 치킨집
N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

# 현재 치킨집 위치 모두 파악
totalChicken = []
for i in range(N):
    for j in range(N):
        if ary[i][j] == 2:
            totalChicken.append((i,j))

# 치킨집 백트래킹, 치킨집 좌표 넣을거임
trace = []
# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값
result = float('INF')

def dfs(start):
    global result

    # 치킨집 설치가 모두 된 경우
    if len(trace) == M:
        minDistance = [[float('INF') for _ in range(N)] for _ in range(N)]

        # 추적된 치킨집들에서 '집'까지의 최소 거리를 구해서 minDistance[][]에 저장
        for t in trace:
            # '집' 과 '치킨집' 과의 거리
            for i in range(N):
                for j in range(N):
                    if ary[i][j] == 1:
                        minDistance[i][j] = min(minDistance[i][j], abs(i - t[0]) + abs(j - t[1]))

        # 추적된 M개의 조합에서, 도시의 치킨 거리 구하기
        _min = 0
        for i in range(N):
            for j in range(N):
                if ary[i][j] == 1: # 집일 때, minDistance[][] 계산
                    _min += minDistance[i][j]

        result = min(result, _min)
        return

    # 집들과의 거리 계산 필요
    for idx in range(start, len(totalChicken)):
        # 0 : 치킨집의 x좌표, 1: y좌표
        trace.append((totalChicken[idx][0], totalChicken[idx][1]))
        dfs(idx+1)
        trace.pop()

dfs(0)
print(result)