T = int(input())

for _ in range(T):
    lst = list(map(str, input().split()))

    lst[0] = float(lst[0])

    for i in range(1, len(lst)):
        if lst[i] == "@":
            lst[0] *= 3
        elif lst[i] == "%":
            lst[0] += 5
        elif lst[i] == "#":
            lst[0] -= 7

    print("{:.2f}".format(lst[0]))