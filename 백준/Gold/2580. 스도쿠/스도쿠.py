## 설마 시간초과 났던 이유가? check9부터 조건 검사를 해서..??

# range(nx, nx+3)도 일단 정답 코드로 바꾸는데, 나머지는 다 로직이 똑같은데 시간초과라니.. 기준을 도저히 모르겠다.. 
# 도저히 기준을 모르겠다.. ㅎㅎ

# 조건 : 스도쿠 채우는 방법이 여럿인 경우는 그 중 하나만을 출력해야 한다..
# 백트래킹으로 풀어야 함..

# 시간초과 : 바로 'k'가 들어가지 못하면 False를 return 한다.
# nx, ny로 시간을 조금 더 단축한다..

import sys
input = sys.stdin.readline

def check9(x, y, k):
    nx = 3 * (x // 3)
    ny = 3 * (y // 3)

    for i in range(3):
        for j in range(3):
            if ary[nx + i][ny + j] == k:
                return False

    return True


def checkRow(x, k):
    for j in range(9):
        if ary[x][j] == k:
            return False

    return True


def checkCol(y, k):
    for i in range(9):
        if ary[i][y] == k:
            return False

    return True


def dfs(count):
    # 모든 '0'에 값을 할당했을 시
    if count == len(zero):
        for k in range(9):
            print(*ary[k])

        # 프로그램 강제 종료
        # return을 하게 되면, 가능한 스도쿠 답이 계속 출력하게 된다.
        exit()

    x = zero[count][0]
    y = zero[count][1]

    for k in range(1, 10):
        # 스도쿠, 3개의 조건을 모두 만족할 시 0 → k로 바꿔준다.
        if checkRow(x, k) and checkCol(y, k) and check9(x, y, k):
            ary[x][y] = k
            dfs(count+1)

            # dfs가 깊이를 충족하지 못하는 경우
            # 백트래킹으로, 0으로 초기화하고 다른 적절한 값을 찾는다.
            # cf. 깊이를 충족하는 경우에도 0으로 초기화하기는 함.
                   # 그래서 깊이를 충족할 때 스도쿠 값들을 전부 출력한다.
            ary[x][y] = 0

# ----------------------------------------------------------
# 현재 스도쿠 상태
ary = [list(map(int, input().split())) for _ in range(9)]

# 스도쿠에서 비어있는 칸 (i,j) 좌표 저장
zero = []
for i in range(9):
    for j in range(9):
        if ary[i][j] == 0:
            zero.append((i,j))

dfs(0)