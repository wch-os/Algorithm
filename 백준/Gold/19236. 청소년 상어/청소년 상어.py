# 풀이 시간 : 2시간 15분
# 시간복잡도 : O(n)
# 공간복잡도 : O(n)
# 참고 : -

# 1. 상어가 (0, 0) 물고기를 먹는다. 이 때 (0, 0) 물고기의 방향을 갖는다.
# 2. 1~16번 물고기가 이동한다.
    # *. 물고기가 이동할 때 45도 방향을 바꾼다면, 바꾼 방향을 지니고 있어야 한다.
# 3. 상어가 지닌 방향으로 이동하여 먹는다.
    # *. 이동 경우의 수는 해당 방향의 전체이다. → 백트래킹 / 상어가 먹는 시점에서 하나의 분기가 나오므로, 리스트의 deepcopy가 필요하다.
    # *. empty이거나 수조를 탈출하면 끝이다.

import copy
import sys
sys.setrecursionlimit(10**6)

result = 0
dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1],
            [1, 0], [1, 1], [0, 1], [-1, 1]]

# O(4*4*8)
# i번 물고기를 이동해주는 함수
def fishSwap(board, idx):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == idx: # idx번 인지 확인
                fishDir = board[x][y][1]

                for k in range(8):
                    # 물고기 이동이 불가하면 45도 방향으로 계속 회전하기
                    resultDir = (fishDir + k) % 8
                    nx = x + dirs[resultDir][0] # 움직여야 할 x 방향
                    ny = y + dirs[resultDir][1] # 움직여야 할 y 방향

                    if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != "shark": # 이동이 가능하고, 상어가 없을 시
                        board[x][y][1] = resultDir # !!. 바뀔 물고기는 45도 방향으로 바꾼 각도여야 한다.
                        board[x][y], board[nx][ny] = board[nx][ny], board[x][y] # swap
                        break

                return board

    return board # 물고기 번호가 없을 경우 그대로 반환



# O(16 * fishSwap)
# 1~16번 물고기 모두를 이동해주는 함수
def fishMove(board):
    # 숫자가 작은 물고기부터 차례대로 움직인다.
    for i in range(1, 17):
        board = fishSwap(board, i) # 각 idx번 물고기를 이동시킨다.


    return board



# O(depth*3 * fishMove)
# 물고기를 이동시키고, 상어가 각 분기에 따라 물고기를 먹는 함수(백트래킹)
def sharkDfs(x, y, board, sharkEat, sharkDir):
    global result
    result = max(result, sharkEat)

    fishMove(board) # 1~16번 물고기를 이동시킨다.

    for k in range(1, 4): # 상어를 이동시킨다.
        nx = x + dirs[sharkDir][0] * k
        ny = y + dirs[sharkDir][1] * k

        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != "empty" : # 물고기가 있어야 한다.
            tmp = board[nx][ny]

            board[x][y] = "empty" # 이전 상어 위치는 물고기가 들어올 수 있는 빈 공간이 된다. (물고기 o, 상어 x)
            board[nx][ny] = "shark" # 상어 이동

            sharkDfs(nx, ny, copy.deepcopy(board), sharkEat + tmp[0], tmp[1])

            board[x][y] = "shark" # 백트래킹 종료, 복원
            board[nx][ny] = tmp



def main():
    board = []
    for _ in range(4):
        lst = []
        k = list(map(int, input().split()))
        for i in range(0, len(k), 2):
            lst.append([k[i], k[i + 1] - 1])  # 물고기 번호, 물고기 방향
        board.append(lst)

    # (0,0) 물고기를 먹고 시작한다.
    tmp = board[0][0]
    board[0][0] = "shark"
    sharkDfs(0, 0, copy.deepcopy(board), tmp[0], tmp[1])



if __name__ == "__main__":
    main()
    print(result)