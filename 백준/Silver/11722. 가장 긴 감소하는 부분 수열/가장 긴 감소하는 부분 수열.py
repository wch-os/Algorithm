N = int(input())
lst = list(map(int, input().split()))

# dp[i] : i 지점의 값에서 '가장 긴 감소하는 부분 수열의 길이'
# 0 인덱스 기준
# dp[0] : lst[0] 지점보다 작은 값은 본인 자신

dp = [1] * N

for i in range(0, N):
    for j in range(0, i):
        # 감소하는 경우이고
        # 이전 dp값들을 보면서 갱신이 필요할 때
        if lst[i] < lst[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

        # 감소 or 갱신이 불필요한 경우일 시, 그대로~
        else:
            continue

print(max(dp))