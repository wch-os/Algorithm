# 재채점. 비용 합이 0인 경우도 정답이 될 수 있으므로,
    # dp[i][j]에서 j의 범위를 0부터 설정해야 한다.

# 풀이 : Knapsack 풀이와 똑같이 풀었다.
# 지난 코드 문제점
    # '필요한 바이트 수(M)'를 dp[][j], 배낭의 크기로 생각하고 접근
        # M의 범위는 천만이므로 시간∙공간 복잡도가 매우 높음
        # 따라서, "비용"을 배낭의 크기로 생각하고 접근하는 것이 효율적이다.

# 직전 코드는 왜 틀렸지?
    # dp[i][j]에서 M바이트를 처음 확보했을 때, 비용 출력하는 코드

# 메모리 개수, 필요한 바이트 수
N, M = map(int, input().split())

memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
sumCost = sum(cost)

# dp[i][j] : i번째 메모리까지 보았을 때, n비용을 사용하면서 얻을 수 있는 최대 바이트 수
dp = [[0] * (sumCost+1) for _ in range(N+1)]
dp[0][0] = 0 # 0비용을 사용하면서 얻을 수 있는 최대 바이트 수는 '0'

# M바이트를 확보하는데 필요한 최소 비용
result = float('inf')

# 각 메모리마다 목표하고자 하는 sumCost까지의 dp[]를 갱신한다.
for i in range(1, N+1):
    for j in range(0, sumCost+1):
        # 현재 앱의 cost가 j보다 클 경우, 앱을 활성화 시킨다.
        if cost[i] > j:
            dp[i][j] = dp[i-1][j]

        else:
            # 현재 앱을 활성화 시켰을 때의 byte vs 비활성화 시켰을 때의 byte를 비교한다.
            # dp[i-1][j] vs j - cost[i]만큼의 비용을 사용할 때 얻을 수 있는 최대 바이트 + 현재 memory[i]만큼 확보할 수 있는 메모리 바이트
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + memory[i])

        # 필요한 메모리 M을 충족시켰을 때, 최소 비용 구하기
        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else: # 필요한 메모리 수가 '0'일 때
    print(0)