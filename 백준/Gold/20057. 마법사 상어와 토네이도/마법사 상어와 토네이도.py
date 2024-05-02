# https://dev-cheddung.tistory.com/103

import math

N = 0  # 격자 크기
sand = 0  # 모래의 양
cDir = 0  # 현재 방향(좌측부터 시작)
num = 1  # 현재 이동 크기
A = []  # 격자
cR, cC = 0, 0  # 현재 위치
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌, 하, 우, 상

# 확산 방향과 비율
diff = [
    [(-1, 1, 1), (1, 1, 1), (-2, 0, 2), (2, 0, 2), (0, -2, 5), (-1, 0, 7), (1, 0, 7), (-1, -1, 10), (1, -1, 10)],  # 좌
    [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, 2, 2), (2, 0, 5), (0, -1, 7), (0, 1, 7), (1, -1, 10), (1, 1, 10)],  # 하
    [(-1, -1, 1), (1, -1, 1), (-2, 0, 2), (2, 0, 2), (0, 2, 5), (-1, 0, 7), (1, 0, 7), (-1, 1, 10), (1, 1, 10)],  # 우
    [(1, -1, 1), (1, 1, 1), (0, -2, 2), (0, 2, 2), (-2, 0, 5), (0, -1, 7), (0, 1, 7), (-1, -1, 10), (-1, 1, 10)],  # 상
]


def move():
    global sand, cR, cC
    cR, cC = cR + dir[cDir][0], cC + dir[cDir][1]
    remain = A[cR][cC]

    for i in range(9):
        nR, nC, percent = cR + diff[cDir][i][0], cC + diff[cDir][i][1], diff[cDir][i][2]
        value = math.trunc(A[cR][cC] * percent / 100)
        if nR < 0 or nR >= N or nC < 0 or nC >= N:
            sand += value
        else:
            A[nR][nC] += value
        remain -= value

    aR, aC = cR + dir[cDir][0], cC + dir[cDir][1]
    if aR < 0 or aR >= N or aC < 0 or aC >= N:
        sand += remain
    else:
        A[aR][aC] += remain
    A[cR][cC] = 0


def tornado():
    global num, cDir, cR, cC
    cR, cC = N // 2, N // 2

    while num < N:
        for _ in range(2):
            for _ in range(num):
                move()
            cDir = (cDir + 1) % 4
        num += 1

    num -= 1
    for _ in range(num):
        move()


def main():
    global N, A
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]
    tornado()
    print(sand)


if __name__ == "__main__":
    main()
