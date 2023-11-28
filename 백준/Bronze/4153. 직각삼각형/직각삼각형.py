import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))

    if sum(lst) == 0:
        break

    long = max(lst)
    _sum = 0
    for k in lst:
        if k != long:
            _sum += pow(k, 2)

    if _sum == pow(long,2):
        print("right")
    else:
        print("wrong")