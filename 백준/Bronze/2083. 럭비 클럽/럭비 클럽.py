import sys
input = sys.stdin.readline

while True:
    lst = list(input().split())

    if lst[0] == '#' and lst[1] == '0' and lst[2] == '0':
        break

    if 17 < int(lst[1]) or 80 <= int(lst[2]):
        print(lst[0] + " Senior")

    else:
        print(lst[0] + " Junior")