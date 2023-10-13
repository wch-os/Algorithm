import sys
input = sys.stdin.readline

n1 = int(input()) # 추의 개수
weight = list(map(int, input().split())) # 추의 무게들

n2 = int(input()) # 확인하고자 하는 구슬의 개수
see = list(map(int, input().split())) # 구슬의 무게들

# dp[추의 개수][측정 가능한 무게]
dp = [[0] * (500*n1+1) for i in range(n1+1)]

def solve(c, w):
    # 저장된 값이 있으면 return
    if dp[c][w] != 0:
        return

    # 지금 w의 무게는 측정이 가능함을 표시
    dp[c][w] = 1

    # 모든 추를 사용할 경우
    # 해당 무게까지 '측정 가능'을 표시한 후, 모든 추를 사용하는지 여부를 판단해야 함!!
    if c == n1:
        return

    solve(c+1, w + weight[c]) # 오른쪽 저울에 올린 경우
    solve(c+1, abs(w - weight[c])) # 왼쪽 저울에 올린 경우
    solve(c+1, w)  # 현재 인덱스의 추를 사용하지 않는 경우

solve(0, 0)

result = []
for s in see:
    # 구슬이 측정 가능 범위 이상의 무게이면
    if s > 500 * 30:
        result.append('N')
    elif dp[n1][s] == 1:
        result.append('Y')
    else:
        result.append('N')

print(*result)