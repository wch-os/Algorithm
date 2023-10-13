# solve() 종료 조건을 1 차이로 다르게 설정함.
  # 이 과정에서 indexError를 방지하기 위해 weight[c-1]로 설정

import sys
input = sys.stdin.readline

n1 = int(input()) # 추의 개수
weight = list(map(int, input().split())) # 추의 무게들

n2 = int(input()) # 확인하고자 하는 구슬의 개수
see = list(map(int, input().split())) # 구슬의 무게들

# dp[추의 개수][측정 가능한 무게]
dp = [[0] * (500*n1+1) for i in range(n1+1)]

def solve(c, w):
    # 모든 추를 사용할 경우
    # 'c==n1' 경우를 포함시켜, dp[c][w]를 갱신하게 만든다.
       # But, weight[c]가 index over가 나지 않도록 weight[c-1]로 수정하여 weight[-1]로도 탐색할 수 있게 한다.
    if c > n1:
        return
    
    # 저장된 값이 있으면 return
    if dp[c][w] != 0:
        return

    # 지금 w의 무게는 측정이 가능함을 표시
    dp[c][w] = 1

    solve(c+1, w + weight[c-1]) # 오른쪽 저울에 올린 경우
    solve(c+1, abs(w - weight[c-1])) # 왼쪽 저울에 올린 경우
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