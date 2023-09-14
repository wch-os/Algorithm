# 백트래킹으로 풀어봤으니, 라이브러리 사용해서 조합으로 풀기

import itertools
import sys
input = sys.stdin.readline

# N*N 도시, M개의 치킨집
N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨집 위치 모두 파악
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if ary[i][j] == 1:
            house.append((i,j))
        elif ary[i][j] == 2:
            chicken.append((i,j))

result = float('INF')
for c_set in itertools.combinations(chicken, M):

    sumDis = 0
    # 1개의 집에서 가장 가까운 치킨집 찾기
    for h in house: # 각 집들

        minDis = float('INF')
        for c in c_set: # M개의 치킨집 중, 1개
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            minDis = min(minDis, dis)

        # 각각의 집에서 가까운 치킨집들의 거리 합
        sumDis += minDis

    result = min(result, sumDis)

print(result)