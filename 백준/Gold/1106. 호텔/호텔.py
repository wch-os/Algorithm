# 풀이 시간: 35분 + 30분
# 시간복잡도: O(NC)
    # N개의 도시 중 홍보할 수 있는 도시를 선택해서, 최소 비용으로 C명을 유치할 수 있는지 체크한다.
    # dp[i][j] : i번째 도시까지의 경우의 수 중, j명을 유치하기 위한 최소비용
# 공간복잡도: O(NC)
# 유형: dp(knapsack)
# 참고: https://frog-in-well.tistory.com/31

# 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구하는 프로그램

# k = 0/1 에 따라 비교식이 다른 이유
# k = 0일 때
    # else 문이 무조건 1번 실행 된다.
    # 따라서 dp[i][j] = min(dp[i][j], dp[i-1][j]) 에서 이전 최솟값인 dp[i-1][j]로 초기화가 진행된다.
    # 그래서 if 문에 걸렸을 대에도, 기존 값에 대한 min 처리가 필요가 없다.

# k = 1일 때
    # else 문이 실행될지 안될지 모른다.

    # else 문 실행
        # 갱신된 dp[i][j] 값 또한, min() 조건이 되므로 추가를 해주어야 한다.
        # if 문에서 갱신된 dp[i][j]에 대한 min() 조건 추가를 해주어야 한다.

    # else 문 실행 안됨
        # if 문에서 기존 dp[i-1][j]에 대한 min() 조건 추가를 해주어야 한다.

def solve():
    for i in range(1, N+1):
        w = board[i][0]  # 홍보 비용
        v = board[i][1]  # 고객 유치 수

        for j in range(1, C+1):

            # 같은 지역에서 계속 홍보할 수 있으므로
            k = 0
            while True:
                # j명 이상으로 유치 성공
                if j <= k * v:
                    # k = 1: dp[i][j] = min(dp[i][j], dp[i-1][j], k * w)
                    dp[i][j] = min(dp[i][j], k * w) # k = 0
                    break
                # j명까지 유치 미달
                else:
                    # k = 1: dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i-1][j-k*v] + k*w)
                    dp[i][j] = min(dp[i][j], dp[i-1][j - k * v] + k * w) # k = 0
                k += 1

    return dp[N][C]



C, N = map(int, input().split())

# N개의 도시 중 홍보할 수 있는 도시를 선택해서, 최소 비용으로 C명을 유치할 수 있는지 체크한다.
# dp[i][j] : i번째 도시까지의 경우의 수 중, j명을 유치하기 위한 최소비용
dp = [[float('inf')] * (C+1) for _ in range(N+1)]

# 홍보 비용, 고객 유치 수
board = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

print(solve())
