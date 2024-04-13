import sys
input = sys.stdin.readline

def postSearch(sticker, r, c, cnt):
    global result

    if cnt == 4:
        return

    R, C = r, c
    sr, sc = 0, 0
    # 회전하기
    rotate = True

    while True:
        post = True
        for i in range(sr, R):
            for j in range(sc, C):
                if 0 > i or i >= N or 0 > j or j >= M: # 스티커의 범위가 보드판의 범위를 벗어나면 안 된다.
                    post = False
                    break
                if sticker[i-sr][j-sc]:
                    if board[i][j]:
                        post = False
                        break

        # 스티커 붙이기
        if post:
            for i in range(sr, R):
                for j in range(sc, C):
                    if 0 <= i < N and 0 <= j < M:  # 스티커의 범위가 보드판의 범위를 벗어나면 안 된다.
                        if sticker[i-sr][j-sc]:
                            board[i][j] = 1
                            result += 1

            rotate = False
            break

        # 스티커 못 붙였을 경우
        else:
            sc += 1
            C += 1
            if C > M:
                sc, C = 0, c
                sr += 1
                R += 1

            if R > N:
                break


    if rotate:
        rotateSticker = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if sticker[i][j]:
                    rotateSticker[j][r-i-1] = 1
        postSearch(rotateSticker, c, r, cnt+1)

    else:
        return


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]

result = 0
for k in range(K):
    n, m = map(int, input().split())

    
    stick = [list(map(int, input().split())) for _ in range(n)]
    postSearch(stick, n, m, 0)
        
print(result)