# 풀이 시간 : 1시간 30분
# 시간복잡도 : O(n^3)
# 공간복잡도 : O(n^2)
# 참고 코드 : -

import sys
input = sys.stdin.readline

# 인근 5평 대여 비용 구하기
def calFive():
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            cost = ary[i][j]
            for z in range(1, 5):
                cost += ary[i + di[z]][j + dj[z]]

            costAry[i][j] = cost


# 모든 꽃잎이 필 수 있는 상황인지 체크
def check(i, j):
    for z in range(5):
        ni = i + di[z]
        nj = j + dj[z]

        # 범위 바깥 or 이미 방문했을 경우
        if not (0 <= ni < N and 0 <= nj < N) or visited[ni][nj]:
            return False

    # 다 필 수 있음
    return True


# 꽃 3개가 정상적으로 필 때까지, 백트래킹 탐색
def dfs(flower, costSum):
    global minCost

    # 꽃 3개가 정상적으로 필 경우
    if flower == 3:
        minCost = min(minCost, costSum)
        return

    # 꽃잎이 피어나는 지역. 방문 처리
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # 꽃이 정상적으로 필 경우
            if check(i,j):
                # 백트래킹 방문 처리
                for z in range(5):
                    ni = i + di[z]
                    nj = j + dj[z]

                    visited[ni][nj] = True

                result.append((i, j))
                dfs(flower+1, costSum + costAry[i][j])
                result.pop()

                # 유효한 경로가 아닐 경우, 미방문 처리
                for z in range(5):
                    ni = i + di[z]
                    nj = j + dj[z]

                    visited[ni][nj] = False

N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)] # input 저장
costAry = [[0] * N for _ in range(N)] # cost[i][j] : 인근 5개의 구역 비용합

di = [0,-1,0,0,1]
dj = [0,0,-1,1,0]
visited = [[False] * N for _ in range(N)]

result = [] # 3개의 꽃 인덱스를 담을 리스트
minCost = float('inf')

calFive() # 5평 대여비용 구하기
dfs(0,0) # 3개의 꽃이 완전히 피어나는 경우 구하기

print(minCost)