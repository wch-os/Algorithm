import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

_sum = 0

# dp[i] : lst의 i-1 인덱스까지의 합
dp = [0]
for i in range(1, len(lst)+1):
    _sum += lst[i-1]
    dp.append(_sum)

for _ in range(M):
    # 구간 정의
    s, e = map(int, input().split())

    # s부터 e까지의 합
    # 0부터 e-1 인덱스까지의 합(dp[e]) - 0부터 s-2 인덱스까지의 합(dp[s-1])
    result = dp[e] - dp[s-1]

    print(result)