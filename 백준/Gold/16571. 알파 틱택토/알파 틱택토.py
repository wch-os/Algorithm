# 풀이 시간: 2시간
# 시간복잡도: O(2^9 * a)
# 공간복잡도: O(9)
# 유형: backtracking
# 참고: https://iamheesoo.github.io/blog//algo-boj16571

# 일반적인 백트래킹과 접근을 달리한다.
# '상대방이 게임을 끝낼 수 있는가?'를 상태로 두고, 그 과정에서 '승/무/패'를 우선순위화 하기 위해 min() 함수를 사용한다.
# 초기 잘못된 접근으로 일정한 규칙 하에 움직이는 그리디로 생각했고, 이후에는 백트래킹으로 NQueen처럼 일정 구역을 회피해야 되는지 생각했다.

""" '틱택토'가 완성되었는지 체크하는 함수 """
def checkFinish(now):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == now:
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == now:
            return True

    if board[0][0] == board[1][1] == board[2][2] == now: return True
    elif board[0][2] == board[1][1] == board[2][0] == now: return True

    return False


""" now에 두는 수가 최선의 수(게임을 끝낼 수 있는 수)가 될 수 있도록 계속해서 재귀 백트래킹 """
def backtracking(now):
    # 상대방의 최선의 승패
    # -1: Loss / 0: Draw / 1: Win
    minis = 2

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = now

                # 내가 이기면, 상대방은 진다.
                if checkFinish(now):
                    board[i][j] = 0
                    return 1

                else:
                    """
                    - 재귀 backtracking은 상대방의 승패를 return 받는다. 즉, return 받는 결과값 그 자체가 minis이다.
                    - min()을 사용하는 이유
                        - 패배하는 수보다는 무승부하는 수가 더 낫다.
                        - 이를 위해, 패배하는 경우(1)를 무승부하는 경우(0)로 덮어쓰기 위해 min()을 사용한다.
                    """
                    minis = min(minis, backtracking(2 if now == 1 else 1))

                board[i][j] = 0


    """
    - minis는 상대방의 최선의 승패에 따라, 나의 승패를 return 한다.
    """
    if minis == 1: return -1
    elif minis == 0 or minis == 2: return 0
    else: return 1
                    


board = [list(map(int, input().split())) for _ in range(3)]

zeroCnt = 0
for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            zeroCnt += 1

# 0이 홀수면, x 선공
win = backtracking(1 if zeroCnt % 2 else 2)

if win == 1: print("W")
elif win == 0: print("D")
else: print("L")