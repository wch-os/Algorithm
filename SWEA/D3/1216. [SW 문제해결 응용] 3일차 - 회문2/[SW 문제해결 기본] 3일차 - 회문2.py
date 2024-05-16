# 풀이 시간 : 50분
# 시간복잡도 : O(N^2)
# 공간복잡도 : O(N^2)
# 참고 : -


SIZE = 100
def palindrome(lst):
    global result
    
    stack = []
    lens = len(lst)
    
    for i in range(lens-1):
        stack.append((i, i, False))
        if lst[i] == lst[i+1]:
            stack.append((i, i+1, True))
    stack.append((lens-1, lens-1, False))
    
    
    while stack:
        x, y, twoJudge = stack.pop() # 팰린드롬 x, y 좌표
        k = 1  # k - 1: 추가된 횟수
        
        while True:
            if 0 < x - k < lens and 0 < y + k < lens and lst[x - k] == lst[y + k]:  # 펠린드롬일 때
                k += 1
            else:
                if twoJudge: # 두글자 회문이었을 경우
                    k = (k - 1) * 2 + 2
                else:
                    k = (k - 1) * 2 + 1

                result = max(result, k)
                break



for _ in range(10):
    T = int(input())
    board = list(input() for _ in range(SIZE))
    roateBoard = [''.join([board[i][j] for i in range(SIZE)]) for j in range(SIZE)]
    board.extend(roateBoard)

    result = 0
    for i in range(SIZE*2):
        palindrome(board[i])

    print(f"#{T} {result}")
