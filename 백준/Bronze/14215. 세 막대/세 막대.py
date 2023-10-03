lst = list(map(int, input().split()))


while True:
    if max(lst) < sum(lst) - max(lst):
        print(sum(lst))
        break

    else:
        for i in range(len(lst)):
            if lst[i] == max(lst):
                lst[i] -= 1
                break