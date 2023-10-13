# 참고 : https://velog.io/@e_juhee/python-%EB%B0%B1%EC%A4%80-11049-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-DP
# 1인덱스 시작이므로 행렬의 길이는 "2(idx 1부터 시작, 행렬곱 가능할 때)~N+1"이다.
import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0,0]]

# 행렬의 크기 입력받음
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append([r,c])

# i번째부터 j번째 행렬까지 곱했을 때 필요한 곱셈 연산의 최솟값
dp = [[0] * (N+1) for _ in range(N+1)]

for k in range(2, N+1): # 행렬의 길이
    for i in range(1, N+1 - k+1): # 출발지
        minValue = float('inf')

        # 행렬 길이 = k이면
        # 시작점이 i일 때, 도착점은 i+k-1이다. (본인 행렬 포함)

        ## 1번째 방법
        # for j in range(k-1):
        #     minValue = min(minValue, dp[i][i+j] + dp[i+j+1][i+k-1] + matrix[i][0] * matrix[i+j][1] * matrix[i+k-1][1])

        ## 2번째 방법
        for j in range(i, i+k-1):
            minValue = min(minValue, dp[i][j] + dp[j+1][i+k-1] + matrix[i][0] * matrix[j][1] * matrix[i+k-1][1])

        dp[i][i+k-1] = minValue

print(dp[1][N])