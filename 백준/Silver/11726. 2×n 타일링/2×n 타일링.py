import sys
sys.setrecursionlimit(10**9)

def fibo(n):
    if n == 0 or n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]

    dp[n] = (fibo(n-1)+ fibo(n-2)) % 10007

    return dp[n] % 10007

N = int(input())
dp = [-1] * (N+1)
print(fibo(N))