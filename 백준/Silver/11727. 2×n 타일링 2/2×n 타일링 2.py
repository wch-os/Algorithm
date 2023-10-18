# 나머지 계산을 안 함..

def fibo(n):
    if dp[n] != 0:
        return dp[n]

    # dp[n-2]에서 - * 2 or ㅁ, 총 2가지의 경우가 있다.
    dp[n] = (fibo(n-1) + 2 * fibo(n-2)) % 10007

    return dp[n]
# 2 * n
n = int(input())

# dp[i] : 2*n 크기의 직사각형을 채우는 방법의 수
dp = [0] * (n + 1)

dp[1] = 1
if n > 1:
    dp[2] = 3
fibo(n)

print(dp[n])