T = int(input())

for _ in range(T):
    r, e, c = map(int, input().split())

    if r == e - c:
        print("does not matter")
    elif r < e - c:
        print("advertise")
    else:
        print("do not advertise")