# 풀이 시간: 40분(생각) + 1시간(참고 및 풀이)
# 시간복잡도: O(2^10 * 10^2)
# 공간복잡도: O(2^10)
# 유형: 그리디
# 참고: https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-14939-%EB%B6%88-%EB%81%84%EA%B8%B0

import copy

# 보드판을 True/False로 초기화하는 함수
def initBoard():
    for i in range(10):
        line = input()

        for j in range(10):
            if line[j] == "O":
                board[i][j] = True


# (x, y) 스위치를 눌렀을 때, 반경 전구의 변화를 반영하는 함수
def press(board, x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 10 and 0 <= ny < 10:
            board[nx][ny] = not board[nx][ny]


# 메인 알고리즘 함수: 1번째 행의 경우 2^10 경우의 수를 고려 + 2~10번째 행은 바로 위의 전구가 켜져있을 때를 고려한다.
def solve():
    for i in range(1 << 10):
        cnt = 0
        newBoard = copy.deepcopy(board)

        # 1번째 줄 경우의 수에 해당하는 전구를 누른다.
        for j in range(10):
            if i & (1 << j):
                press(newBoard, 0, j)
                cnt += 1

        # 2 ~ 10번째 줄의 경우는, 바로 위의 전구가 켜져있을 때 누른다.
        for x in range(1, 10):
            for y in range(10):
                if newBoard[x-1][y]: # 바로 위 전구 켜짐.
                    press(newBoard, x, y)
                    cnt += 1

        # 10번째 줄에 불이 켜져 있지 않으면
        if not any(newBoard[9]):
            pressCount[i] = cnt



board = [[False] * 10 for _ in range(10)]
pressCount = [101] * (1<<10) # 2^10 경우의 수에서, 모든 전구를 끄기 위해 '최소한으로 눌러야 하는 스위치 개수'를 저장

dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]

# board를 True/False로 초기화
initBoard()

# 문제 풀이
solve()

result = min(pressCount)
if result == 101:
    print(-1)
else:
    print(result)