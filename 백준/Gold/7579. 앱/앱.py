# 풀이 : Knapsack 풀이와 똑같이 풀었다.
# 지난 코드 문제점
    # '필요한 바이트 수(M)'를 dp[][j], 배낭의 크기로 생각하고 접근
        # M의 범위는 천만이므로 시간∙공간 복잡도가 매우 높음
        # 따라서, "비용"을 배낭의 크기로 생각하고 접근하는 것이 효율적이다.
        
# 직전 코드는 왜 틀렸지?
    # dp[i][j]에서 M바이트를 처음 확보했을 때, 비용 출력하는 코드

# 메모리 개수, 필요한 바이트 수
N, M = map(int, input().split())

mi = [0] + list(map(int, input().split()))
ci = [0] + list(map(int, input().split()))
sumCost = sum(ci)

# dp[i][j] : i번째 메모리까지 보았을 때, n비용을 사용하면서 얻을 수 있는 최대 바이트 수
dp = [[0] * (sumCost+1) for _ in range(N+1)]
dp[0][0] = 0 # 0비용을 사용하면서 얻을 수 있는 최대 바이트 수는 '0'

# M바이트를 확보하는데 필요한 최소 비용
result = float('inf')

# 각 메모리마다 목표하고자 하는 sumCost까지의 dp[]를 갱신한다.
for i in range(1, N+1):
    for j in range(1, sumCost+1):
        # 비용을 체크함으로써, 메모리를 추가할 수 있을 때
        if ci[i] <= j:
            # dp[i-1][j] vs j - ci[i]만큼의 비용을 사용할 때 얻을 수 있는 최대 바이트 + 현재 mi[i]만큼 확보할 수 있는 메모리 바이트
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-ci[i]] + mi[i])

        # j의 비용이 부족해, 메모리를 추가할 수 없을 때 → 이전 최적값으로 설정
        else:
            dp[i][j] = dp[i-1][j]

        # 필요한 메모리 M을 충족시켰을 때, 최소 비용 구하기
        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else: # 필요한 메모리 수가 '0'일 때
    print(0)
