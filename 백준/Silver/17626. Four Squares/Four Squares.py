# 풀이 시간 : 15분
# 시간복잡도 : O(N*sqrt(N)) → 1100만?
# 공간복잡도 : O(n^2)
# 참고 : -

# 점화식을 세우자.. ㅎㅎ
import math
import sys
input = sys.stdin.readline

N = int(input())

# dp[i] : 합이 i가 되는 제곱수들의 최소 갯수
    # 점화식
    # dp[n] = min(dp[n], dp[n-제곱수] + 1)
    # 제곱수가 n보다 작을 때까지 비교
dp = [float('inf') for _ in range(N+1)]

for i in range(int(math.sqrt(N))+1):
    dp[i*i] = 1

# 각 dp값 구하기
for i in range(1, N+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-(j*j)] + 1)

print(dp[N])