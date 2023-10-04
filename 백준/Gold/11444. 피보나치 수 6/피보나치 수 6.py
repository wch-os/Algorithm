# 참고 : https://st-lab.tistory.com/251
# 마지막에 "% 1000000007" 안해줘서..??


# 행렬 거듭제곱
def mulmatrix(a, b):
    # 행렬 곱셈 결과를 담을 배열
    temp = [[0] * 2 for _ in range(2)]

    # 행렬 곱셈
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += ((a[i][k] * b[k][j]) % 1000000007)

    return temp


def solve(k):
    # conquer 할 시점
    if k == 1:
        return A

    # k == 1일 때까지 계속 분할
    o = solve(k // 2)

    # 모듈러 연산
    if k % 2 == 0:
        return mulmatrix(o, o)

    else:
        return mulmatrix(mulmatrix(o, o), A)


# 피보나치 수를 행렬 거듭제곱으로 나타내면
# F(n+2) = [1, 1] * [F(n+1), F(n)] → 전치
# F(n+1) = [1, 0] * [F(n+1), F(n)] → 전치
# [F(n+2), F(n+1)] → 전치 = [[1, 1], [1, 0]] * [F(n+1), F(n)] → 전치
# 즉, U(n+1) = A * U(n)
# 따라서, U(n) = A^n * U(0)
A = [[1, 1], [1, 0]]

n = int(input())

# U(0) = [1, 0]
# 마지막 A^n * U(0)을 진행하고 남은 값은 result[1][0]이다.
result = solve(n)
print(result[1][0] % 1000000007)