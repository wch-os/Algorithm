import sys

input = sys.stdin.readline


def solve():
    dx = [1, 0] # 오른쪽, 위
    dy = [0, 1]

    for i in range(N):
        for j in range(N):
            if result[i][j] != 0: #도착 경로가 있으면

                # (N-1, N-1)은 이전에 갱신되어 !=0이 된다.
                # 따라서 아래 계산에서 *2가 되는데 이 경우를 계산에서 제하기 위해 배제하는 코드를 작성한다.
                if i==N-1 and j==N-1:
                    continue

                K = matrix[i][j] # 보드에 적혀있는 수

                # 현재위치에서 K만큼 오른쪽으로 이동한 좌표
                if i+K < N:
                    result[i+K][j] += result[i][j]  # 이전 경로의 경우 수를 더해준다.

                if j+K < N:
                    result[i][j+K] += result[i][j]  # 이전 경로의 경우 수를 더해준다.



if __name__ == '__main__':
    N = int(input()) # 게임판의 크기
    matrix = [list(map(int, input().split())) for _ in range(N)] # 게임판 입력
    result = [[0]*N for _ in range(N)] # 각 지점까지 도착할 수 있는 경로 체크

    result[0][0] = 1 # (0,0) 출발
    solve()

    print(result[N-1][N-1]) # (N-1, N-1)까지 도착할 수 있는 경로 수 출력