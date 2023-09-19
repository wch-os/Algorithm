# 참고 : https://nahwasa.com/entry/%EB%88%84%EC%A0%81-%ED%95%A9prefix-sum-2%EC%B0%A8%EC%9B%90-%EB%88%84%EC%A0%81%ED%95%A9prefix-sum-of-matrix-with-java

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
prefixSum = [[0]*(N+1) for _ in range(N+1)]

# prefixSum 구하기
# prefixSum 인덱스는 1 시작, matrix 인덱스는 0 시작이므로
# 자신의 인덱스 값(matrix[i][j])을 더할 때 대입받은 prefixSum 인덱스에서 -1 해줌으로써 맞춰준다.
for i in range(1, N+1):
    for j in range(1, N+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i-1][j-1]



for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # (x2,y2) 누적합 - (x1-1, y2) 누적합 - (x2, y1-1) 누적합 + (x1-1, y1-1) 누적합
    result = prefixSum[x2][y2] - prefixSum[x1-1][y2] - prefixSum[x2][y1-1] + prefixSum[x1-1][y1-1]
    print(result)
