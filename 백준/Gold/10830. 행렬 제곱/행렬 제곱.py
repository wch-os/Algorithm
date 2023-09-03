import sys
input = sys.stdin.readline

N, mul = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def matrix_mul(A, B):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += (A[i][k] * B[k][j])

            temp[i][j] %= 1000 #연산 비용을 줄이기 위해... 추가

    return temp

def solve(mul):
    while True:
        if mul == 1:
            return matrix

        else:
            # A^(mul) = A^(mul//2) * A^(mul//2) 로 나눈다.
            o = solve(mul // 2)

            # 짝수일 경우
            if mul%2 == 0:
                return matrix_mul(o, o)

            # 홀수일 경우
            else:
                temp =  matrix_mul(o, o)
                return matrix_mul(temp, matrix)


# 문제에서 요구하는 Matrix 출력
resultMatrix = solve(mul)
resultMatrix = [[k % 1000 for k in row] for row in resultMatrix]

for row in resultMatrix:
    print(*row)