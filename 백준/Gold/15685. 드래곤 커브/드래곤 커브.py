# 풀이 시간 : 40분 + 50분(사각형 생각, 문제 요구 X) + 30
# 시간복잡도 : O(2^g + 100*100*4)
# 공간복잡도 : O(100*100)
# 참고 : https://tmdrl5779.tistory.com/146
    # → 세대에 따라 모양이 변할 때, stack.pop()이 아니라 list에서 역순으로 접근해서 푸는 코드이다.

# Point!
    # x, y 좌표를 바꿀 것
    # curve 90도 규칙성

# 추가로 생각할 것
    # 문제 : 네 꼭짓점이 모두 드래곤 커브의 일부인 경우
    # 간선으로 둘러싼 정사각형 개수를 출력하라고 하면?

import sys
input = sys.stdin.readline

# → ↑ ← ↓
# arrow = [(0, 1), (-1, 0), (0, -1), (1, 0)]
arrowX = [0, -1, 0, 1]
arrowY = [1, 0, -1, 0]
visited = [[0 for _ in range(101)] for _ in range(101)]

def move(x, y, stack):
    for i in stack:
        x += arrowX[i]
        y += arrowY[i]

        visited[x][y] = 1

    # if not stack:
    #     return
    #
    # i = stack.pop()
    #
    # nx = x + arrowX[i]
    # ny = y + arrowY[i]
    #
    # visited[nx][ny] = 1
    # move(nx, ny, stack)


def check():
    squareCnt = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
                squareCnt += 1

    return squareCnt

def main():
    N = int(input()) # 커브 개수

    for _ in range(N):
        # (x, y) : 커브 시작점 / d : 시작 방향 / g : 세대
        y, x, d, g = map(int, input().split())
        visited[x][y] = 1

        stack = [d]
        turnStack = [d]
        for _ in range(g):
            # 현재 그려져 있는 그림을 90도로 회전시키고, 기존 그림과 합친다
            while turnStack:
                idx = turnStack.pop() # 기존 그림 회전
                idx = (idx + 1) % 4
                stack.append(idx) # 기존 그림과 합친다.

            # 현재 그림을, n세대까지 다시 회전시키기 위함
            turnStack = stack.copy()

        move(x, y, stack)

if __name__ == "__main__":
    main()
    print(check())