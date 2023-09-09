import sys
input = sys.stdin.readline

N = int(input())
children = list(map(int, input().split()))

# dp[i] = i 번호일 때까지 연속된 증가수열의 개수
# dp[i] = dp[i-1] + 1
dp = [0] * (N+1)

cqMax = 0
for i in range(len(children)):
    dp[children[i]] = dp[children[i]-1] + 1

dp.sort()
print(N-dp[N])


# 5
# 5 2 1 3 4
# int[] dp = new int[6]
# dp[5] = dp[4]+1;
# dp[2] = dp[1]+1;
# dp[1] = dp[0]+1;
# dp[3] = dp[2]+1;
# dp[4] = dp[3]+1;
# 를 거쳐 dp = {0, 1, 1, 2, 3, 1};