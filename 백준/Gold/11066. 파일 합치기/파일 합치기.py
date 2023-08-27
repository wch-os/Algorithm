#참고
#https://data-make.tistory.com/402

import sys
input = sys.stdin.readline

T = int(input()) # 테스트케이스 갯수

for _ in range(T):
    N = int(input()) # 소설 장 수
    K = [0] + list(map(int, input().split())) # 소설 파일 크기

    sum = [0] * (N+1)

    # 파일 누적 합
    for i in range(N):
        sum[i+1] = sum[i] + K[i+1]

    # dp 배열 정의
    # dp[i][j] : i에서부터 j까지의 파일 크기 최소합
    # dp[i][k] + dp[k+1][j] + sum(A[i]~A[j])
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(2, N + 1):  # 부분 파일의 길이
        for j in range(1, N + 2 - i):  # 시작점
            #dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + (sum[j + i - 1] - sum[j - 1])

            min_value = float('inf')
            for k in range(i - 1): #중간 인덱스
                current_value = dp[j][j + k] + dp[j + k + 1][j + i - 1]
                min_value = min(min_value, current_value)
            dp[j][j + i - 1] = min_value + (sum[j + i - 1] - sum[j - 1])

    print(dp[1][N])