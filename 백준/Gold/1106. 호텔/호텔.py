# 풀이 시간: 35분 + 30분 + 20분
# 시간복잡도: O(NC)
    # N개의 도시 중 홍보할 수 있는 도시를 선택해서, 최소 비용으로 C명을 유치할 수 있는지 체크한다.
    # dp[i][j] : i번째 도시까지의 경우의 수 중, j명을 유치하기 위한 최소비용
# 공간복잡도: O(NC)
# 유형: dp(knapsack)
# 참고: https://frog-in-well.tistory.com/31


def solve():
    for i in range(1, N+1):
        w = board[i][0]  # 홍보 비용
        v = board[i][1]  # 고객 유치 수

        # "적어도 C명 유치"라는 뜻은 C명 그 이상의 고객을 유치해도 된다.
        # 1개의 도시에서 유치할 수 있는 최대 고객은 100명이므로, C+100까지 dp[]값을 구해야 한다.
        for j in range(v, C+100):
            # 이전 dp 값을 N개를 만들지 않고, 슬라이드처럼 계속 활용한다.
            # 이전 i 고객을 유치하기 위한 최소 비용 vs j - v 까지 유치하는데 드는 비용 + i 도시에서 v만큼 유치하는데 드는 비용
            dp[j] = min(dp[j], dp[j - v] + w)

    return min(dp[C:])



C, N = map(int, input().split())

# 최소 비용으로 C명을 유치할 수 있는지 체크한다.
# dp[i] : i명을 유치하는데 드는 최소 비용
dp = [float('inf')] * (C + 100)
dp[0] = 0

# 홍보 비용, 고객 유치 수
board = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

print(solve())
