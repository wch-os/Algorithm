# 처음에 거리 2를 기준으로 접근
# 백트래킹, 완전탐색

import sys
input = sys.stdin.readline

N = int(input())

ary = [list(map(int, input().split())) for _ in range(N)]
costAry = [[0] * N for _ in range(N)]

di = [0,-1,0,0,1]
dj = [0,0,-1,1,0]
visited = [[False] * N for _ in range(N)]

def backtrack(flower):
    global minCost

    # 꽃 3개가 정상적으로 필 경우
    if flower == 3:
        nowCost = 0
        
        # 꽃을 심기 위한 최소 비용 출력
        for idx in range(len(result)):
            a, b = result[idx]
            nowCost += costAry[a][b]

        minCost = min(minCost, nowCost)
        return


    # 꽃잎이 피어나는 지역. 방문 처리
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            result.append((i, j))  # 꽃 중심좌표 append 하기 (정상적으로 핀다고 가정하고)

            # 모든 꽃잎이 필 수 있는 상황인지 체크
            count = 0
            for z in range(5):
                ni = i + di[z]
                nj = j + dj[z]

                if 0 <= ni < N and 0 <= nj < N:
                    if not visited[ni][nj]:
                        count += 1

            # 꽃 3개가 정상적으로 필 경우
            if count == 5:
                # 백트래킹 방문 처리
                for z in range(5):
                    ni = i + di[z]
                    nj = j + dj[z]

                    if 0 <= ni < N and 0 <= nj < N:
                        if not visited[ni][nj]:
                            visited[ni][nj] = True

                backtrack(flower+1)
                result.pop() # 계산 후, pop() 하기

                # 유효한 경로가 아닐 경우, 미방문 처리
                for z in range(5):
                    ni = i + di[z]
                    nj = j + dj[z]

                    if 0 <= ni < N and 0 <= nj < N:
                        if visited[ni][nj]:
                            visited[ni][nj] = False

            else: # (정상적으로 피지 못할 경우, pop())
                result.pop()


result = []
minCost = float('inf')


for i in range(1, N-1):
    for j in range(1, N-1):
        cost = ary[i][j]
        for z in range(1, 5):
            ni = i + di[z]
            nj = j + dj[z]

            cost += ary[ni][nj]

        costAry[i][j] = cost

backtrack(0)
print(minCost)