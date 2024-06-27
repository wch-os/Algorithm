# 풀이 시간: 20분 + 10분
# 시간복잡도: O(2^N * N^2)
# 공간복잡도: O(N^2)
# 유형: greedy, bitmasking
# 참고: -

# 14939와 유사한 문제

# 시간초과
    # copy.deepcopy를 쓰지 않고, `newBoard = [board[i][:] for i in range(N)]`를 사용했다.

def press(newBoard, x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            newBoard[nx][ny] = 1 - newBoard[nx][ny]


def solve():
    global result

    for i in range(1 << N):
        cnt = 0
        newBoard = [board[i][:] for i in range(N)]

        # 1. i 비트마스킹 경우에 따른 1번째 줄 전구 스위치 누르기
        for j in range(N):
            if i & (1 << j):
                press(newBoard, 0, j)
                cnt += 1

        # 2. 2 ~ N번째 줄, 현재 위치의 윗 전구가 켜져있을 때 전구 스위치 누르기
        for x in range(1, N):
            for y in range(N):
                if newBoard[x-1][y]:
                    press(newBoard, x, y)
                    cnt += 1

        # 3. 마지막 N번째 줄에 전구가 꺼져있으면, i 경우에 대해서 성공이다.
        if not any(newBoard[N-1]):
            result = min(result, cnt)



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]

result = float('inf')
solve()

print(-1 if result == float('inf') else result)