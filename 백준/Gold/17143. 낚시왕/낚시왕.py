# 풀이 시간: 1시간 50분 + 30분
# 시간복잡도: O(C * M * speed (=10억)) 시간초과?
    # C: 100 / M: 10000 / speed: 1000
    # 왕 상어 포획: O(C)
    # 상어 이동: O(M * speed) => 규칙을 찾아 최소화 필요
    # 중복 상어: O(R * C)
    # 이 모든 것을 C번 반복
# 공간복잡도: O(R * C)
# 유형: 구현, 시뮬레이션
# 참고: -
import copy
# 1. 왕이 오른쪽으로 한 칸 이동, C칸 도착 시 종료
# 2. board[king][0 ~ R-1] 칸 중 상어 1마리 잡는다.
# 3. 상어가 이동한다.
    # 같은 칸에 위치 시 크기를 비교해, 1마리만 남겨둔다.

# 틀렸습니다.
    # 기존 상어를 맵에서 지울 때, (x, y)가 바뀌기 전에 먼저 지워야 함 (리팩토링 과정에서 실수했다..)
    # 상어가 이동했을 때, 아직 이동 전의 상어가 있을 수도 있으므로 newBoard를 통해 갱신을 해야 함

import sys
input = sys.stdin.readline

def solve():
    # 위, 오른쪽, 아래, 왼쪽
    global board

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    king = 0  # 왕의 위치
    catchSize = 0 # 지금까지 잡은 상어 크기의 합
    deadSharks = [] # 죽은 상어 List

    while True:
        # 1. 왕이 이동을 한다.
        king += 1

        # 2. 왕이 상어를 잡는다.
        for i in range(1, R + 1):
            if board[i][king]:
                deadSharks.append(board[i][king][0][0])
                catchSize += board[i][king][0][1]
                board[i][king].clear()
                break

        # 2-1. 왕의 위치가 C칸에서 상어를 잡으면 끝이 난다.
            # 문제 정의에서는 (C+1)칸까지 도달해야 끝이 나지만, 그 이후의 상어의 이동은 의미가 없으므로 C칸에서 상어를 잡고 끝내도록 한다.
        if king == C:
            return catchSize

        # 3. 상어 이동하기
        newBoard = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
        for shark in sharks:

            # 이미 죽은 상어일 경우
            if shark[0] in deadSharks:
                continue

            # 상어 | x좌표, y좌표, 속력, 이동방향, 상어 크기
            x, y, s, d, z = shark[1], shark[2], shark[3], shark[4], shark[5]

            for _ in range(s):
                x += dx[d] # 방향대로 1칸 이동
                if not 1 <= x <= R:
                    d = (d + 2) % 4
                    x += 2 * dx[d] # 1칸을 이미 갔으므로, 그 반대로 2칸을 간다.

                y += dy[d]
                if not 1 <= y <= C:
                    d = (d + 2) % 4
                    y += 2 * dy[d]

            shark[1], shark[2], shark[4] = x, y, d # 바뀐 값들을 갱신해주도록 한다.
            newBoard[x][y].append((shark[0], z)) # 이동한 상어 배치

            
        # 3-1. 이동을 마친 후 board 칸에 상어가 2마리 있는지 체크
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                
                if len(newBoard[i][j]) >= 2:
                    # 가장 크기가 큰 상어 찾기
                    maxSharkIdx, maxSharkSize = 0, 0
                    for k in newBoard[i][j]:
                        if maxSharkSize < k[1]:
                            maxSharkIdx, maxSharkSize = k[0], k[1]
                    
                    # 나머지 작은 상어는 전부 먹힌다.
                    for k in newBoard[i][j]:
                        if maxSharkSize != k[1]:
                            deadSharks.append(k[0])

                    # 가장 크기가 큰 상어만 남기도록 한다.
                    newBoard[i][j].clear()
                    newBoard[i][j].append((maxSharkIdx, maxSharkSize))

        board = copy.deepcopy(newBoard)

                            

# R, C: 격자판의 크기 / M: 상어의 수
R, C, M = map(int, input().split())

board = [[[] for _ in range(C+1)] for _ in range(R + 1)]

# r, c: 상어의 위치 / s: 속력 / d: 이동방향 / z: 크기
sharks = []
for i in range(1, M + 1):
    one = [i] + list(map(int, input().split()))

    one[4] -= 1 # 0 인덱스로 조정 (%로 방향을 조절하기 위함)
    if one[4] == 1: one[4] = 2 # (동서 / 남북 대칭 인덱스를 위함)
    elif one[4] == 2: one[4] = 1
    sharks.append(one)

    board[one[1]][one[2]].append((i, one[5])) # 상어 checkIdx, 크기

print(solve())