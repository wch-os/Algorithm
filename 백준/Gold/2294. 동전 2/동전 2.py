# 틀린 이유 : dp[coin] = 1을 초기화하는 과정에서, coin이 k보다 클 경우 indexError가 발생한다.
# 시간복잡도 : O(NK)
# 공간복잡도 : O(N), O(K)

import sys
sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# '동전 0' 문제에서는 dp[i] : i가치를 만드는데 필요한 동전의 경우의 수
# dp[i] : i가치를 만드는데 필요한 동전의 최소 개수
dp = [float('inf')] * (k+1)

# 각각의 동전은 1개로 자신의 가치를 만들 수 있음
for coin in coins:
    if coin <= k:
        dp[coin] = 1

# dp[i]를 구하기 위해, dp[i-coin]의 경우의 수를 더함
for i in range(n):
    for j in range(coins[i], k+1):
        # 지난 값 vs j-coin[i]가치를 만드는데 필요한 동전의 경우의 수 + 1(coin[i] 개수 추가)
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[k] != float('inf'):
    print(dp[k])
else: # 만들 수 없는 가치일 경우
    print(-1)