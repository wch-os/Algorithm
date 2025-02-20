from collections import deque

"""문제 해결"""
def solve():
    move = 0 # 인구 이동 횟수
    while True:
        visited = [[False] * N for _ in range(N)]
        moveOperation = False

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    unionList, unionValue = bfs(i, j, visited)

                    """!. 자신을 제외한 합칠 수 있는 영역이 있어야 함"""
                    if len(unionList) > 1:
                        moveOperation = True
                        unionCalCulate(unionList, unionValue)

        if moveOperation:
            move += 1
        else:
            return move



"""합칠 수 있는 영역 및 인구 구하기"""
def bfs(i, j, visited):
    unionList = [(i, j)] # 합칠 수 있는 영역
    unionValue = board[i][j] # 합칠 수 있는 총 인구

    visited[i][j] = True
    q = deque()
    q.append((i, j))

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < N) and not visited[nx][ny]:
                """!. 여기 라인에서 visited[nx][ny] = true를 해버리면, 다른 노드에서 탐색이 가능한 경우도 탐색을 하지 못하는 문제가 발생한다."""
                # 범위 내의 오차일 경우 합친다.
                diff = abs(board[x][y] - board[nx][ny])
                if minRange <= diff <= maxRange:
                    """!. 정확히 합칠 수 있다고 판단이 되었을 때, true로 표시를 하도록 한다."""
                    visited[nx][ny] = True
                    unionList.append((nx, ny))
                    unionValue += board[nx][ny]
                    q.append((nx, ny))


    return unionList, unionValue


"""합친 영역의 인구 평균 맞추기"""
def unionCalCulate(unionList, sumValue):
    avgValue = sumValue // len(unionList)

    for nodeX, nodeY in unionList:
        board[nodeX][nodeY] = avgValue



N, minRange, maxRange = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = solve()
print(result)
