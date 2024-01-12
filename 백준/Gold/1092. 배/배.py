N = int(input())
crane = list(map(int, input().split()))

M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

time = 0
if crane[0] < box[0]:
    print(-1)

else:
    while box:
        for c in crane:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break

        time += 1

    print(time)
