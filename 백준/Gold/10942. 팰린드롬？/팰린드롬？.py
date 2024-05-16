# 풀이 시간 : 45분
# 시간복잡도 : O(N^2)
# 공간복잡도 : O(N^2)
# 참고 : -

# 빠른 입력
# 집중하자!

import sys
input = sys.stdin.readline

def palindrome():
    for _ in range(len(stack)):
        k = 1

        a, b = stack.pop()
        while True:
            if 0 <= a - k < N and 0 <= b + k < N:
                if lst[a - k] != lst[b + k]:
                    break
                dp[a - k][b + k] = 1
                k += 1
            else:
                break



N = int(input())
lst = list(map(int, input().split()))

stack = []
dp = [[0] * N for _ in range(N)]
for i in range(N-1):
    dp[i][i] = 1
    stack.append((i, i))

    # 초기에 짝수 팰린드롬도 체크
    if lst[i] == lst[i+1]:
        stack.append((i, i+1))
        dp[i][i+1] = 1

# 마지막 인덱스 체크
dp[N-1][N-1] = 1
stack.append((N-1, N-1))

palindrome()

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
