# k==1 조건 코드 제외 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0] + [int(input()) for _ in range(N)]

# dp[i][j] = i개의 배열로, j개의 구간을 선택했을 때 구간합 최댓값
    # 배열을 이루는 수에는 음수도 있음
dp = [[0] + [-float('inf')] * M for _ in range(N+1)]

# 점화식
# 1. 구간을 유지하면서 i번째 값을 포함시키지 않았을 경우
# dp[i][j] = max(dp[i][j], dp[i-1][j])
# 2. 새로운 구간으로 i번째 값을 포함시켰을 경우, 하지만 간격이 있어야 하므로
# dp[i][j] = max(dp[i][j], dp[k-2][j-1] + sum[i] - sum[k-1])

# 구간합 구하기
rangeSum = []
sumI = 0
for i in range(N+1):
    sumI += lst[i]
    rangeSum.append(sumI)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i - 1][j]
        for k in range(1, i+1):
            # k>=2일 때, 구간 간격을 띄울 수 있음
            if k >= 2:
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + rangeSum[i] - rangeSum[k-1])

            # 1개의 구간일 때는 총합 값이다.
            elif j == 1:
                dp[i][j] = max(dp[i][j], rangeSum[i])

print(dp[N][M])