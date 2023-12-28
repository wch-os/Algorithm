# 풀이 시간 : 47분
# 시간복잡도 : O(N^3)
# 공간복잡도 : O(N^2)
# 참고 : -

# 생각
    # 랜덤 지점에서, 랜덤 지점까지 갈 수 있는지를 체크해야 한다.
    # 플로이드 알고리즘으로 minDis[][] = '최소거리', 모든 노드에서의 최소 거리를 구한다.
    # minDis[s][e] 를 출력한다.


import sys
input = sys.stdin.readline

FIX = 10000

# n : 건물의 수, m : 길의 수
n, m = map(int, input().split())

minDis = [[FIX] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    minDis[u][v] = 0 # 단방향
    minDis[v][u] = 1 # 일단 1로 초기화, 양방향으로 바뀌는 것을 체크

    if b == 1: # 양방향
        minDis[v][u] = 0

for i in range(1, n+1):
    minDis[i][i] = 0 # 자기자신은 '0'

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 양방향일 시 그냥 지나가고, 단방향일 시 +1 카운트
                # 구해야 할 것은 최소 몇 개의 일반통행 길을 양방향 통행으로 바꿔야 하는가? → 주어지지 않는 도로는 제외한다.(FIX)
            # 따라서 minDis[i][j]는 "양방향 통행으로 바꿔야 할 단방향 도로의 갯수"가 저장된다.
            if minDis[i][k] != FIX and minDis[k][j] != FIX:
                minDis[i][j] = min(minDis[i][j], minDis[i][k] + minDis[k][j])



# 각 질문에 대해, 최소 몇 개의 일방통행 길이 양방향 통행으로 바꿔야 출발지에서 도착지로 갈 수 있는지를 출력
k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(minDis[s][e])