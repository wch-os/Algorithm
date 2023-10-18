# 참고 : https://mygumi.tistory.com/135
# 더 낮은 시간복잡도 : O(KN)

N, K = map(int, input().split())
MOD = 1000000000

# dp[i][j] : i개의 숫자를 이용해, j를 만드는 경우의 수
dp = [[0] * (N+1) for _ in range(K+1)]

# 1개만 사용해서 i를 표현하는 경우의 수는 "1개"뿐이다.
for i in range(N+1):
    dp[1][i] = 1

# dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j]
#                 j          j-1                 0 을 더하면 됨
for i in range(2, K+1): # 몇 개를 선택했냐?, 1개만 사용하는 경우는 초기화했으므로 2개부터 계산한다.
    for j in range(N+1): # 0~N까지 만들 수 있는 경우의 수를 모두 체크한다.
        #for k in range(j+1):
        #dp[i][j-1] 값이 이미 dp[i-1][0]부터 dp[i-1][i-j]까지의 합을 반영한 값이다.
            dp[i][j] += dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= MOD

print(dp[K][N])