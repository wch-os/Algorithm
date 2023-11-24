# 풀이 시간 : 1시간 30분
# 시간복잡도 : O((N/2) * (5B + RC))
    # N회 반복
    # 홀수 : bfs 폭탄 터지기 (5개 간선, 폭탄 개수 B)
    # 짝수 : 모든 칸 폭탄 설치 (R행, C열)
# 공간복잡도 : O(RC)
# 참고 : -

# 1초 - 초기 상태
# 2초 - 폭탄이 설치되어 있지 않은 모든 칸 폭탄 설치
# 3초 - '초기 폭탄'의 인접 지역 펑!
# 4초 - 폭탄이 설치되어 있지 않은 모든 칸 폭탄 설치
# 5초 - 2초에 설치된 폭탄 펑!
# 6초 - 폭탄이 설치되어 있지 않은 모든 칸 폭탄 설치
# 7초 - 4초에 설치된 폭탄 펑!

from collections import deque

# row, col, N초가 지난 후
R, C, N = map(int, input().split())

# 띄어쓰기 없는 입력값, 2차원 배열에 저장
lst = []
for i in range(R):
    sen = []
    for s in input():
        sen.append(s)
    lst.append(sen)

bombs = deque() # 터트릴 폭탄을 저장할 큐

time = 1
while True:
    # N초가 지났으면(N초까지의 행동이 끝났으면) 격자판 출력
    if time == N+1:
        for row in lst:
            for x in row:
                print(x, end="")
            print()
        break

    if time == 1:
        time += 1
        continue

    # 1초를 제외한, 홀수 초에 폭탄이 터진다.
    if time % 2 == 1:
        # 펑 터트리기
        visited = [[False] * C for _ in range(R)]
        dx = [0, 0, 0, 1, -1]
        dy = [0, 1, -1, 0, 0]

        while bombs:
            x, y = bombs.popleft()

            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0<=nx<R and 0<=ny<C) and (not visited[nx][ny]):
                    visited[nx][ny] = True
                    lst[nx][ny] = '.'

    # 모든 지역 폭탄 설치
    elif time % 2 == 0:
        # 폭탄을 설치하기 이전에, 현재(다음에 터트릴) 폭탄 위치 저장하기
        for i in range(R):
            for j in range(C):
                if lst[i][j] == 'O':
                    bombs.append((i, j))
                lst[i][j] = 'O'

    # 째깍째깍
    time += 1