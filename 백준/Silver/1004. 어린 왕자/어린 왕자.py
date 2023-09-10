import sys
from math import sqrt
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 출발지, 목적지 좌표
    x1, y1, x2, y2 = map(int, input().split())

    # 행성계 개수
    planet = int(input())

    # 출발지에서 목적지까지 가기 위해 필요한 '최소 진입/이탈 횟수'
    count = 0
    for _ in range(planet):
        # 행성계 (a,b) 좌표, 반지름
        a, b, r = map(int, input().split())

        # 출발점과, 도착점에서 | 행성 중앙까지의 거리
        disS = sqrt(pow(x1-a, 2) + pow(y1-b, 2))
        disE = sqrt(pow(x2-a, 2) + pow(y2-b, 2))

        # 출발점과 도착점이 둘 다 행성계 내부에 있을 경우는 pass
        if disS < r and disE <  r:
            continue
        # 한 쪽만 행성계 내부에 있을 경우는, 1번의 진입/이탈이 필요하다
        elif disS < r or disE <  r:
            count += 1

    print(count)