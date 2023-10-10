import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(N)] # N*M 크기

M, K = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(M)] # M*K 크기

result = [[0] * K for _ in range(N)] # N*K 크기

for k in range(K):
    for i in range(N):
        for j in range(M):
            result[i][k] += matrixA[i][j] * matrixB[j][k]

for row in result:
    print(' '.join(map(str, row)))