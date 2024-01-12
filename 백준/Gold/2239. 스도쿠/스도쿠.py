# 풀이 시간 : 1시간
# 시간복잡도 : O(9*9*9 - X)
# 공간복잡도 : O(9*9)
# 참고 : -

# 스도쿠의 조건
    # 행, 열, 네모칸 모두 1가지 숫자만 있는 것

# 완전탐색
    # 시간복잡도 = O(9*9*9)
    # 백트래킹으로 넣었다 뺐다 하면 단축되지 않을까?
    # k 값은 스도쿠 값으로, range(1, 10)으로 설정해줘야 함

# 와.. 인덱스 설정 틀려서 20분 넘게 잡아먹었네..

lst = [list(map(int, input())) for _ in range(9)]
cnt = 0

def check(row, col, num):
    for i in range(0, 9):
        if lst[row][i] == num:
            return False

    for i in range(9):
        if lst[i][col] == num:
            return False

    quotR = row // 3
    quotC = col // 3

    for i in range(3):
        for j in range(3):
            if lst[3*quotR+i][3*quotC+j] == num:
                return False

    return True


def dfs(R, C):
    global cnt
    global finalX, finalY
    if finalX == R and finalY == C:
        for i in range(9):
            for j in range(9):
                print(lst[i][j], end="")
            print()
        exit()


    for i in range(9):
        for j in range(9):
            # 빈 칸 넣기
            if lst[i][j] == 0:
                for k in range(1, 10):
                    if check(i, j, k):
                        lst[i][j] = k
                        dfs(i, j)
                        lst[i][j] = 0

                    # 1~9 까지 모두 안 되었을 경우, 이전 lst[i][j] 값을 다른 값을 넣어줘야 함
                    # cf. check[9] == True 일 때, final까지 계속 dfs 탐색함.
                    if k == 9:
                        return


finalX = 0
finalY = 0
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            finalX = i
            finalY = j

dfs(0, 0)