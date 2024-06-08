# 풀이 시간: 1시간 + 30분(정답)
# 시간복잡도: O(1)
# 공간복잡도: O(1)
# 유형: dp
# 참고: https://welog.tistory.com/362

# 이전 풀이의 복잡도는 10^8이 아니라, 10^15였다.

# dp[i]: 성냥개비 i개를 사용해서 만들 수 있는 가장 작은 수
# 점화식
    # dp[i] = min(dp[i], dp[i-j] * 10 + dp[j])
    # dp[i-j] * 10: j(2~7)를 뺀 값에서 자리 이동을 시킨 값
    # dp[j]: 1의 자리 값


import sys
input = sys.stdin.readline

T = int(input())
dp = [float('inf')] * 101
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6 # 0으로 시작할 수 없으므로, 초기값은 6
dp[7] = 8
dp[8] = 10

def low(n):
    for num in range(9, 101):
        for j in range(2, 8):
            if j == 6:
                # 0 이 추가된다.
                dp[num] = min(dp[num], dp[num-j]*10)
            else:
                # dp[j] 자릿수 더해주기
                dp[num] = min(dp[num], dp[num-j]*10 + dp[j])

    print(dp[n], end=" ")


def high(n):
    highMatch = []

    if n % 2:
        highMatch.append(7)
    else:
        highMatch.append(1)

    while n > 3:
        n -= 2
        highMatch.append(1)

    print(*highMatch, sep="")


for i in range(T):
    N = int(input())

    low(N)
    high(N)
