# 주석 수정, for문 범위 설정을 이용한 if문 제거

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i] : i가치를 만드는데의 경우의 수
dp = [0] * (k+1)

# 0원을 만드는데 경우의 수는 1
dp[0] = 1

# 모든 동전에 대해, 목표 가치 k번까지 경우의 수가 갱신된다.
for i in range(n):
    for j in range(coins[i], k+1):
        # coins[i]를 이용해서 j가치를 만드려면, 그전에 dp[j-coins[i]]를 충족시켜야한다.
        dp[j] += dp[j-coins[i]]

print(dp[k])