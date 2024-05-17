# 풀이 시간 : 40분
# 시간복잡도 : O(NM)
# 공간복잡도 : O(NM)
# 참고 : -

numbers = [
    "0001101",
    "0011001",
    "0010011",
    "0111101",
    "0100011",
    "0110001",
    "0101111",
    "0111011",
    "0110111",
    "0001011"
]


def oneSearch():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if board[i][j] == '1':
                return i, j

def check(x, y):
    stack = [] # pop 하면 숫자 회복 가능
    for _ in range(8): # 7bit의 8개 숫자
        for k in range(10):
            if numbers[k] == board[x][y-6:y+1]:
                stack.append(k)
                break

        y -= 7


    sumEven, sumOdd = 0, 0
    for i in range(0, 8, 2): # 짝수번째 합
        sumEven += stack[i]
    for i in range(1, 8, 2): # 홀수번째 합
        sumOdd += stack[i]

    if ((sumOdd * 3) + sumEven) % 10: # 10의 배수가 아니다.
        return 0
    else:
        return sumEven + sumOdd



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    board = [input() for _ in range(N)]
    oneX, oneY = oneSearch()
    print(f"#{t} {check(oneX, oneY)}")