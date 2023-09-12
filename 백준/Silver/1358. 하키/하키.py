# range(X+W+1) 쓰려던 것을 그대로 가져와서 틀렸다.. ㅎ

import sys
from math import sqrt
input = sys.stdin.readline

# W,H 크기의 직사각형 / (X,Y) 왼쪽 모서리 좌표 / P 선수의 수
W, H, X, Y, P = map(int, input().split())

# 링크 안 or 경계에 있는 선수 몇 명
count = 0
for _ in range(P):
    a, b = map(int, input().split())

    # 직사각형 내에 있는 경우
    if X <= a <= X+W and Y <= b <= Y+H:
        count += 1
        continue

    # 두 원 내에 있는 경우
    R = H/2
    dis1 = sqrt((X-a)**2 + (Y+R-b)**2)

    if dis1 <= R:
        count += 1
        continue

    dis2 = sqrt((X + W - a) ** 2 + (Y + R - b) ** 2)
    if dis2 <= R:
        count += 1
        continue

print(count)