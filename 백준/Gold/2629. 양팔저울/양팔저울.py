# 풀이 시간: 35분
# 시간복잡도: O(3^N - dp 복잡도)
# 공간복잡도: O((500) * N^2)
    # 추 1개 최대 무게 500g
# 유형: dp
# 참고: 이전 풀이

def solve(i, w):
    if dp[i][w]:
        return

    dp[i][w] = True

    # 추 모두 사용
    if i == N:
        return

    solve(i + 1, w + pendulums[i])  # 왼쪽 저울
    solve(i + 1, abs(w - pendulums[i]))  # 오른쪽 저울
    solve(i + 1, w)  # 추를 안 올림.



N = int(input()) # 추의 개수
pendulums = list(map(int, input().split()))

M = int(input()) # 구슬의 개수
beads = list(map(int, input().split()))

# dp[사용한 추 개수][측정 가능한 무게]
dp = [[False] * (500*N+1) for _ in range(N+1)]

solve(0, 0)

for bead in beads:
    if bead > 500 * 30: # 구슬의 무게는 40000보다 작거나 같은 자연수이다. 
        print("N", end=" ")
    elif dp[N][bead]:
        print("Y", end= " ")
    else:
        print("N", end= " ")