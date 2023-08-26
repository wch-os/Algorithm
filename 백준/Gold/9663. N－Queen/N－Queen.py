#참고
#https://seongonion.tistory.com/103

# 크기가 N인 체스판 위에, 퀸 N개를 서로 공격할 수 없게 놓는 문제
N = int(input())

# (i, j)에 퀸을 놓는다면, row[i] = j
count = 0
row = [0] * N

def isPromise(x):
    # 이전 행에 놓여진 퀸들과 비교하기
    for i in range(x):
        # 같은 열에 다른 퀸이 있는 경우 or 대각선에 다른 퀸이 있는 경우(x축 차이 = y축 차이)
        if row[x] == row[i] or x - i == abs(row[x] - row[i]):
            return False

    # 지금까지 놓여진 퀸의 경로와 겹치지 않는다.
    return True


def nQueen(start):
    global count

    # 종료조건, N개의 퀸을 전부 놓았으면 끝
    if start == N:
        count += 1
        return

    else:
        for i in range(N):
            # start 행에 퀸 놓기
            # (start, i) 지점에 퀸 놓기
            row[start] = i

            # 해당 자리가 유망하면
            if isPromise(start):
                nQueen(start+1)

nQueen(0) # 0번째 행부터 퀸 놓기
print(count) # 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수