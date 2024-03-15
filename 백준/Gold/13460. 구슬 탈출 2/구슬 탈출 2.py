# 풀이 시간 : 2시간
# 시간복잡도 : O(8N*result)
# 공간복잡도 : O(NM)
# 참고 : -

# . : 빈 칸
# # : 장애물 or 벽
# 0 : 구멍 위치(*)
# R : 빨간 구슬의 위치
# B : 파란 구슬의 위치

import copy
import sys
from collections import deque
input = sys.stdin.readline

red, blue = 0, 0
N, M = 0, 0

# 시간 복잡도 : O(N)
def redCheck(dx, dy, i, redX, redY, boards):
    redFlag = False

    boards[redX][redY] = '.' # 기존 빨간색 구슬 '.'
    while boards[redX + dx[i]][redY + dy[i]] == '.' or boards[redX + dx[i]][redY + dy[i]] == 'O':
        if boards[redX + dx[i]][redY + dy[i]] == 'O':
            redFlag = True
            return 0, 0, redFlag, boards # (0, 0) 벽으로 의미없는 좌표이므로, 구슬에 빠졌을 때 해당 칸으로 지정
        redX += dx[i]
        redY += dy[i]

    boards[redX][redY] = 'R' # 빨간색 구슬 이동
    return redX, redY, redFlag, boards # (이동한 좌표, 빨간색 구슬이 들어갔는지 유무, 바뀐 보드판)


def blueCheck(dx, dy, i, blueX, blueY, boards):
    blueFlag = False

    boards[blueX][blueY] = '.'  # 기존 파란색 구슬 '.'
    while boards[blueX + dx[i]][blueY + dy[i]] == '.' or boards[blueX + dx[i]][blueY + dy[i]] == 'O':
        if boards[blueX + dx[i]][blueY + dy[i]] == 'O':
            blueFlag = True
            return 0, 0, blueFlag, boards
        blueX += dx[i]
        blueY += dy[i]

    boards[blueX][blueY] = 'B'  # 파란색 구슬 이동
    return blueX, blueY, blueFlag, boards # (이동한 좌표, 파란색 구슬이 들어갔는지 유무, 바뀐 보드판)


# 4방향을 red/blue 이동하므로 8N * 이동 수 result
def bfs():
    visited = set()
    q = deque()
    q.append((red, blue, 0, False, False, board))
    while q:
        r, b, move, rFlag, bFlag, boards = q.popleft()

        # 빨간색 o, 파란색 x
        if rFlag and not bFlag:
            print(move)
            exit()
        # 10번 이상 이동
        elif move > 10:
            print(-1)
            exit()
        # 파란색 구슬이 빠졌으면 다른 길을 모색한다.
        elif bFlag:
            continue

        # 중복 탐색을 방지하기 위해 R(x, y) / B(x, y) 를 네자리수로 표현을 해 두었다.
        visit = r[0] * 1000 + r[1] * 100 + b[0] * 10 + b[1]
        if visit not in visited:
            visited.add(visit)

            dx = [0,1,-1,0]
            dy = [-1,0,0,1]

            for i in range(4):
                redX, redY = r[0], r[1]
                blueX, blueY = b[0], b[1]

                # 무슨 색을 먼저 이동해야 할 지 정한다.
                firstRed = True
                if (i == 0 and redY > blueY) or (i == 1 and redX < blueX) or (i == 2 and redX > blueX) or (i == 3 and redY < blueY):
                    firstRed = False

                if firstRed:
                    # 기울였을 때, 빨간색 구슬이 이동할 수 있으면
                    redX, redY, redFlag, boardChange = redCheck(dx, dy, i, redX, redY, copy.deepcopy(boards))
                    # 다시 파란색 구슬이 이동할 수 있는지 체크
                    blueX, blueY, blueFlag, boardChange = blueCheck(dx, dy, i, blueX, blueY, boardChange)
                else:
                    blueX, blueY, blueFlag, boardChange = blueCheck(dx, dy, i, blueX, blueY, copy.deepcopy(boards))
                    redX, redY, redFlag, boardChange = redCheck(dx, dy, i, redX, redY, boardChange)

                # boards → boardChange 된 보드로 탐색을 해야 한다.
                # 기존 boards 는 for i in range(4) 로 탐색할 수 있는 곳을 찾아야 하기 때문에, 변화되면 안 된다.
                # 따라서 deepcopy를 사용했다.
                q.append(((redX, redY), (blueX, blueY), move+1, redFlag, blueFlag, boardChange))

    # 계속 같은 자리 탐색만 시도해, 큐에 원소가 없어 반복이 끝날 때
    print(-1)


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = []
    for i in range(N):
        row = []
        for s in input():
            row.append(s)
            if s == 'R':
                red = (i, len(row) - 1)

            elif s == 'B':
                blue = (i, len(row) - 1)
        board.append(row)

    bfs()