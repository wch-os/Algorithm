# 풀이 시간 : 45분 + 5분 + 20분
# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n^2 * l)
# 참고 : 질문게시판 반례

# -1, +1 차이로 결과값의 오류가 났는데
# 플로우대로 코드를 작성하면 더 빠르게 풀 수 있었을 것 같다.
# 리팩토링은 정확히 동작한 다음에,,

# 초기 뱀이 있던 자리 '표식'을 해주어야 한다.
# -*
# ** 의 경우에서 4초

# 지나감을 표시 안함.. ㅋㅋ
    # 뱀의 꼬리가 정적인 상태가 되어버림;;
    # queue로 편하게 구현하자

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N+1)]
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

change = []
L = int(input()) # 뱀의 방향 변환 횟수
for _ in range(L):
    T, LR = map(str, input().split())
    T = int(T)
    change.append([T, LR])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y, idx):
    global time

    nx = x + dx[idx]
    ny = y + dy[idx]
    time += 1

    # 뱀이 자기 자신을 만나거나, 벽에 부딪히면
    if (nx < 0 or nx >= N or ny < 0 or ny >= N) or (nx, ny) in snakeList:
        print(time)
        exit()

    # 일단 몸길이를 늘린다.
    snakeList.appendleft((nx, ny))
    # 사과가 있으면, 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    # 사과가 없으면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
    elif board[nx][ny] == 0:
        snakeList.pop()

    # time 초가 끝난 뒤
    for t, lr in change:
        if t == time:
            if lr == "L":
                idx -= 1
                if idx < 0: idx = 3
                break
            else:
                idx += 1
                if idx > 3: idx = 0
                break

    dfs(nx, ny, idx)


time = 0
trace = deque()
snakeList = deque()
snakeList.append([board[0][0]])
dfs(0, 0, 1)