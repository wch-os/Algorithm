# elif else 문으로 시간초과 방지
# 동일 시간 time 처리

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

minV = float('inf')
maxV = 0
for i in range(N):
    minV = min(minV, min(board[i]))
    maxV = max(maxV, max(board[i]))


time = float('inf')
for k in range(minV, maxV+1):
    push = 0
    need = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > k:
                push += (board[i][j] - k)
            else:
                need += (k - board[i][j])

    # B + push에 비해 need가 크다면 해당 높이는 만족할 수 없음 → 더 깎아야 함
    if B + push < need:
        continue

    if time >= push * 2 + need * 1:
        time = push * 2 + need * 1
        high = k

print(time, high)