# 낮 코드에 의미없이 반복하는 코드가 있었다.

# 풀이 시간 : 1시간 30분 + 20분
# 시간복잡도 : O(N*N^2)
# 공간복잡도 : O(N^2)
# 참고 : https://zoosso.tistory.com/418#google_vignette
#       https://yabmoons.tistory.com/348

import sys
input = sys.stdin.readline

def dfs(night, playerCnt):
    global result

    # 마피아가 죽었거나, 마피아 혼자 살아남았을 경우
    if not player[me][1] or playerCnt == 1:
        result = max(result, night)
        return


    # 낮
    if playerCnt % 2:
        target = 0
        maxPoint = -float('inf')
        for i in range(N):
            if player[i][1]:  # 남은 사람 & 살아있는 사람
                if maxPoint < player[i][0]:
                    target = i
                    maxPoint = player[i][0]

        player[target][1] = False
        dfs(night, playerCnt-1)
        player[target][1] = True


    # 밤
    else:
        for i in range(N):
            if not player[i][1] or i == me: # 죽은 사람 or 마피아일 경우
                continue

            player[i][1] = False
            for j in range(N):
                if j == i:
                    continue
                player[j][0] += graph[i][j]

            dfs(night+1, playerCnt-1)

            player[i][1] = True
            for j in range(N):
                if j == i:
                    continue
                player[j][0] -= graph[i][j]


N = int(input())
input_player = list(map(int, input().split()))  # 유죄지수
player = []
for k in input_player:
    player.append([k, True])

graph = [list(map(int, input().split())) for _ in range(N)]
me = int(input())  # 참가자 번호

result = -float('inf')

if N <= 1:
    print(0)
    exit()

dfs(0, N)
print(result)