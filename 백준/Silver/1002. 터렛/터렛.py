import sys
input = sys.stdin.readline

from math import sqrt

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 좌표의 거리
    xyDis = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))

    # 두 반지름의 합
    diameter = r1 + r2

    # 두 원의 중심이 같을 때
    if xyDis == 0:
        # 완전히 겹쳤을 때
        if r1 == r2:
            print(-1)
        # 반지름이 다를 때 고려
        else:
            print(0)

    # 두 원의 중심이 다를 떼
    else:
        # 접점이 1개일 때
        # 내접원일 때 고려
        if xyDis == diameter or (xyDis == abs(r2-r1)):
            print(1)

        # 접점이 2개일 때
        elif abs(r2-r1) < xyDis < diameter:
            print(2)

        # 접점이 0개일 때
        else:
            print(0)