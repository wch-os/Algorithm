N = int(input()) #기관차가 끌고 가던 객차의 수
guest = [0] + list(map(int, input().split())) #각 객차에 타고 있는 손님 수 #인덱스 1 기준이므로 [0] 추가해주어야 한다.
canPull = int(input()) #소형 기관차가 최대로 끌 수 있는 객차의 수

#i번째 소형 기관차가, 객차 j번째까지 보았을 때 / 최대로 운송할 수 있는 승객 수
dp = [[0] * (N+1) for _ in range(3+1)]

#1~N까지 각 손님의 합
for i in range(N):
    guest[i+1] += guest[i]

for i in range(1, 4): #소형기관차 수
    for j in range(i*canPull, N+1): #객차 수
        # 이전 dp(이번 객차를 포함하지 않는 경우) vs 이전 소형기관차가 끌었던 객차까지 승객 수 + 이번 소형기관차가 끄는 객차의 승객 수
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-canPull] + (guest[j] - guest[j-canPull]))

print(dp[3][N])