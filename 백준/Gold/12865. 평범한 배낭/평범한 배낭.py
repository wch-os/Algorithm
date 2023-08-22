def solve():
    for i in range(1, N+1):
        for j in range(1, K+1):
            #배낭에 넣을 수 있을 때
            if w[i]<=j:
                #현재 배낭 무게 vs 현재 무게 - 뺄 수 있는 최적 물건 무게 + 현재 물건 무게
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

            #배낭에 넣을 수 없을 때
              #->이전 배낭 무게로 설정하기
            else:
                dp[i][j] = dp[i-1][j]

if __name__ == '__main__':
    N, K = map(int, input().split()) #물건 수, 버틸 수 있는 무게
    dp = [[0] * (K+1) for _ in range(N+1)]
    thing = [[0,0]] #인덱스 1부터 유효한 값 넣게끔
    w = [0] * (N+1)
    v = [0] * (N+1)

    for i in range(1, N+1):
        thing.append(list(map(int, input().split())))
        w[i] = thing[i][0]
        v[i] = thing[i][1]

    solve()

    print(dp[N][K])