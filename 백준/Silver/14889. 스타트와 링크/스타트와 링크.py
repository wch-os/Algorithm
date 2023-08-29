import itertools

N = int(input())

lst =[i for i in range(0, N)]

matrix = [list(map(int, input().split())) for _ in range(N)] # 시너지 행렬

team1 = []
result = float('INF') #두 팀 능력치 차이의 최솟값

def dfs(start):
    global result

    if len(team1) == N/2:
        # # 팀 멤버 출력하기
        # print(' '.join(map(int, team1)))

        # team1 시너지 합 구하기
        # team1 리스트 순열로 시너지 찾기
        permu1 = itertools.permutations(team1, 2)
        sum1 = 0
        for i, j in permu1:
            sum1 += matrix[i][j]

        team2 = list(set(lst) - set(team1))

        # team2 시너지 합 구하기
        permu2 = itertools.permutations(team2, 2)
        sum2 = 0
        for i, j in permu2:
            sum2 += matrix[i][j]

        # 시너지 최소값
        result = min(result, abs(sum1-sum2))
        return

    for i in range(start, N):
        team1.append(i)
        dfs(i+1)
        team1.pop()

dfs(0)
print(result)