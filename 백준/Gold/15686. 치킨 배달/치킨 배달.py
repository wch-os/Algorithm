# 1번째로 제출한 백트래킹을, 2번 로직을 적용해 house[]을 만들고 간단하게 만듦

import sys
input = sys.stdin.readline

# N*N 도시, M개의 치킨집
N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

# 현재 치킨집 위치 모두 파악
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if ary[i][j] == 2:
            chicken.append((i,j))
        elif ary[i][j] == 1:
            house.append(((i,j)))

# 치킨집 백트래킹, 치킨집 좌표 넣을거임
trace = []
# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값
result = float('INF')

def dfs(start):
    global result

    # 치킨집 설치가 모두 된 경우
    if len(trace) == M:
        sumDis = 0 # 도시의 치킨 거리
        # '집' 과 '치킨집' 과의 거리
        for h in house:
            minDis = float('INF')
            # 추적된 치킨집들에서 '집'까지의 최소 거리
            for t in trace:
                dis = abs(h[0]-t[0]) + abs(h[1]-t[1])
                # 내 집에서 가장 가까운 치킨집 찾기
                minDis = min(minDis, dis)

            sumDis += minDis

        result = min(result, sumDis)
        return

    # 집들과의 거리 계산 필요
    for idx in range(start, len(chicken)):
        # 0 : 치킨집의 x좌표, 1: y좌표
        trace.append((chicken[idx][0], chicken[idx][1]))
        dfs(idx+1)
        trace.pop()

dfs(0)
print(result)