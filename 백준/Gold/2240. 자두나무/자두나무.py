# 풀이 시간: 30분
# 시간복잡도: O(T*W)
# 공간복잡도: O(T*W)
# 유형: dp
# 참고:

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]

"""1) 한 번도 움직이지 않고, 1번 위치에서 자두 받기"""
cnt = 0
for i in range(1, T + 1):
    if jadu[i] == 1:
        cnt += 1
    dp[i][0] += cnt

"""
2) 각 초마다 이동할 수 있는 이동횟수 범위에서 받을 수 있는 최대 자두 개수 구하기
현재 위치에 자두가 없을 시, 움직여서 자두를 받을 것인지 움직이지 않고 자두를 받지 않을 것인지 체크
주의. j가 0 ~ W 범위일 경우 한 번도 움직이지 않는 경우가 고려되지 않는다.
"""
for i in range(1, T + 1):
    for j in range(1, W + 1):
        if j % 2: # 이동 횟수 홀수 → 현재 2번 나무에 위치
            if jadu[i] == 2: # 현재 위치에 자두가 있을 시
                dp[i][j] = dp[i - 1][j] + 1 # 움직이지 않고 자두 get
            else:
                # 움직이고 자두 get | 움직이지 않고 자두 no
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])

        else:
            if jadu[i] == 1:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])


print(dp[T][W])