# 풀이 시간 : 40분 + 10분
# 시간복잡도 : O(13Cm * House 수 * m)
# 공간복잡도 : O(n^2)
# 참고 : -

# Combination 구할 때 비효율적이었다.
# depth로 M을 체크하고, 탐색 인덱스로도 설정하면 3이상으로 올라가지 않아 비효율적으로 탐색한다.
# 따라서 depth(start)는 탐색 인덱스 기능으로 따로 설정하고, M개 체크는 len(store)로 체크하는 것이 좋다.
# 그리고 재귀 dfs 매개변수는 start가 아니라 i

import sys
input = sys.stdin.readline

house = []
store = []
def location():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                house.append((i, j))
            elif board[i][j] == 2:
                store.append((i, j))


def getDistance(mStore):
    cityDis = 0
    for h in house:
        minDis = float('inf')

        for s in mStore:
            shDis = abs(s[0] - h[0]) + abs(s[1] - h[1])
            minDis = min(minDis, shDis)

        cityDis += minDis

    return cityDis


result = float('inf')  # 도시 거리
mStore = []  # M개의 가게를 담을 공간
def dfs(start):
    global result

    if len(mStore) == M:
        cityDis = getDistance(mStore)
        result = min(result, cityDis)
        return


    for i in range(start, len(store)):
        mStore.append((store[i][0], store[i][1]))
        dfs(i+1)
        mStore.pop()



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

location()

dfs(0)
print(result)