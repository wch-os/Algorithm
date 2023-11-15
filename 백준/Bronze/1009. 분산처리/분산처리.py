# 11번째 라인을 놓침..

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    a %= 10 
    
    if a == 1:
        print(1)

    # 2, 4, 8, 16, 32, 64
    elif a == 2:
        if b % 4 == 1:
            print(2)

        elif b % 4 == 2:
            print(4)

        elif b % 4 == 3:
            print(8)

        else:
            print(6)

    # 3, 9, 27, 81, 243
    elif a == 3:
        if b % 4 == 1:
            print(3)

        elif b % 4 == 2:
            print(9)

        elif b % 4 == 3:
            print(7)

        else:
            print(1)

    # 4, 16, 64, 256
    elif a == 4:
        if b % 2 == 1:
            print(4)

        else:
            print(6)

    elif a == 5:
        print(5)

    elif a == 6:
        print(6)

    # 7, 49, 3, 1, 7
    elif a == 7:
        if b % 4 == 1:
            print(7)

        elif b % 4 == 2:
            print(9)

        elif b % 4 == 3:
            print(3)

        else:
            print(1)

    # 8, 4, 2, 6
    elif a == 8:
        if b % 4 == 1:
            print(8)

        elif b % 4 == 2:
            print(4)

        elif b % 4 == 3:
            print(2)

        else:
            print(6)

    # 9, 1
    elif a == 9:
        if b % 2 == 1:
            print(9)

        else:
            print(1)

    else:
        print(10)