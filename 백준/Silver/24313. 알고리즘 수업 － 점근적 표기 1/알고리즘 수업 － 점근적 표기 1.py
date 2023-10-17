a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1-c < 0:
    if -a0 / (a1- c) <= n0:
        print(1)
    else:
        print(0)

elif a1-c == 0:
    if a0 <= 0:
        print(1)
    else:
        print(0)

else:
    print(0)