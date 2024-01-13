# farm[M-1][N-1]에 장애물이 있는 경우, dp[M][N] 값에 결과값이 들어있지 않다.
# 아.. 모두 장애물일 경우
    # result 초기값이 그대로 출력이 되므로
    # result 초기값을 0으로 설정해 주어야 한다.

# 풀이 시간 : 1시간 5분 + 40분
# 시간복잡도 : O(MN)
# 공간복잡도 : O(MN)
# 참고 : https://www.acmicpc.net/source/66884805
#       https://sangdo913.tistory.com/116

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(M)]

# dp[i][j] : i, j 에서 지을 수 있는 가장 큰 정사각형 목장 크기
# dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    # 왼쪽, 위쪽, 왼쪽 위 대각선
dp = [[0] * (N+1) for _ in range(M+1)]

result = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if farm[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            result = max(result, dp[i][j])

print(result)
