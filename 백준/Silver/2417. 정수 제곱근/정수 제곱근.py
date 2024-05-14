# lowerbound 문제
# n 이상인 lowerbound를 찾으면 된다.

def lowerBound():
    lo, hi = -1, num + 1

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if mid ** 2 < num:
            lo = mid
        else:
            hi = mid

    return hi


num = int(input())
print(lowerBound())