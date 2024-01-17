# 내 코드와 뭐가 틀린거지?

import sys
input = sys.stdin.readline

m,n = map(int, input().split())
matrix = [list(map(int, input() .split())) for _ in range(m)]
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
maxFarm = 0

for i in range(1,m+1):
  for j in range(1,n+1):
    if not matrix[i-1][j-1]:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
      maxFarm = max(maxFarm, dp[i][j])

print(maxFarm)