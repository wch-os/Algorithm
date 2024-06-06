# 이전 코드
    # 퀸을 놓을 때 row[x] = y 로 넣음.

# 현재 코드
    # 퀸을 놓을 때 board[x][y] = 1 로 넣음.
    # 별도의 행열 체크하는 연산이 더 들어간다.

def isGood(x):
    for i in range(x):
        # 같은 열
        if row[x] == row[i]:
            return False

        # 대각선
        # 퀸이 놓여 있어야 값이 들어감, 초기값은 0
        if x - i == abs(row[x] - row[i]):
            return False

    return True


result = 0
def nQueen(curr):
    global result

    if curr == N:
        result += 1
        return

    for j in range(N):
        row[curr] = j

        if isGood(curr):
            nQueen(curr + 1)


N = int(input())
row = [0] * N

nQueen(0)
print(result)