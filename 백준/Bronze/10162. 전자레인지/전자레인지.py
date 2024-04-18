T = int(input())

a, b, c = 0, 0, 0

while T != 0:
    if T >= 300:
        T -= 300
        a += 1

    elif T >= 60:
        T -= 60
        b += 1

    elif T >= 10:
        T -= 10
        c += 1

    else:
        print(-1)
        exit()

print(a, b, c)