# 풀이 시간: 30분
# 시간복잡도: O(logN)
# 공간복잡도: O(7*N)
# 유형: divide and conquer
# 참고: -

def solve(start, end, depth):
    if start + 1 == end:
        return

    # 오늘의 동료는 내일의 적이다.
    mid = (start + end) // 2
    for j in range(start, mid): 
        board[depth][j] = not board[depth][j]

    solve(start, mid, depth + 1)
    solve(mid, end, depth + 1)


N = int(input())
board = [[True] * N for _ in range(7)]
solve(0, N, 0)

for i in range(7):
    if all(board[i]): # 각 팀에는 최소 1마리의 원숭이가 있어야 한다.
        board[i][0] = False
        
    for j in range(N):
        if board[i][j]:
            print("A", end="")
        else:
            print("B", end="")

    print()