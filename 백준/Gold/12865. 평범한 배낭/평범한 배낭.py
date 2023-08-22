#참고
#https://hongcoding.tistory.com/50

N, K = map(int, input().split()) # 물건 수, 버틸 수 있는 무게

# 각 물건을 집었을 때, 가방에 차게되는 무게 중 / 최대 용량을 넘지 않으면서, 최대 이익
# 머릿속으로 solve() 실행해보면 이해됨
dp = [[0] * (K+1) for _ in range(N+1)]
thing = [[0,0]] #인덱스 1부터 유효한 값 넣게끔

for i in range(N):
    thing.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1): #현재 배낭에 넣을 수 있는 최대 무게

        # 각 물건 무게, 가치
        w = thing[i][0]
        v = thing[i][1]

        # 지금 물건을, 배낭에 넣을 수 있을 때
        if w <= j:
            # 현재 배낭 무게 vs 현재 무게 - 뺄 수 있는 최적 물건 무게 + 현재 물건 무게
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

        # 배낭에 넣을 수 없을 때 → 이전 배낭 무게로 설정하기
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
