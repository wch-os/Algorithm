# 풀이 시간: 1시간 30분
# 시간복잡도: O(NM)
# 공간복잡도: O(NM)
# 유형: graph, mst, simulation
# 참고: -

"""
1. 각 섬 구분 (bfs)
2. 각 섬 연결 간선 찾기 (N*M 탐색)
3. union-find
"""

import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j, islandIdx, visited):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    q = deque([(i, j)])
    board[i][j] = islandIdx

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = islandIdx
                    q.append((nx, ny))

""" 
O(N*M)
각 섬을 구분하기 위한, 섬 번호를 지정하는 함수 
"""
def distinctIsland():
    islandIdx = 2 # 섬 구분 번호 (1은 입력값이므로, 2부터 시작)

    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i, j, islandIdx, visited)
                islandIdx += 1

    return islandIdx - 1 # 마지막 섬 번호


"""
MST를 찾기 위해 각 섬을 연결하는 간선들을 찾는 함수
O(NM)
"""
def searchIslandEdge():
    for i in range(N):
        cnt = 0
        prevY = -1

        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
            else:
                # 이전 좌표가 초기화 된 좌표가 아니고, 다리 길이가 2 이상인 경우
                if prevY != -1 and cnt >= 2:
                    edges.append((cnt, board[i][prevY], board[i][j]))
                prevY = j
                cnt = 0

    for j in range(M):
        cnt = 0
        prevX = -1

        for i in range(N):
            if board[i][j] == 0:
                cnt += 1
            else:
                # 이전 좌표가 초기화 된 좌표가 아니고, 다리 길이가 2 이상인 경우
                if prevX != -1 and cnt >= 2:
                    edges.append((cnt, board[prevX][j], board[i][j]))
                prevX = i
                cnt = 0


"""
O(a(N))
MST, 그래프 내의 모든 정점을 포함하지만 사이클이 없는 트리를 만들기 위한
union-find 알고리즘 사용
"""
def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)

    parents[rootX] = rootY


def isAllConnected():
    for each in parents[3:]:
        if parents[3] != parents[each]:
            return False

    return True


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    """ 각 섬 구분 """
    islandNum = distinctIsland()

    """ 각 섬(노드) 연결 간선 찾기 """
    edges = []
    searchIslandEdge()
    edges.sort()

    """ 최소 비용으로 모든 노드 연결하기 """
    result, cnt = 0, 1
    parents = [0, 0] + [i for i in range(2, islandNum + 1)]
    for cost, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            result += cost
            cnt += 1


    if result == 0 or cnt != islandNum - 1 :
        print(-1)
    else:
        print(result)

