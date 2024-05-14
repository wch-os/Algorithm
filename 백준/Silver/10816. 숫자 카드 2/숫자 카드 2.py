def lowerBound(num):
    # lo는 lst의 모든 원소가 num보다 클 경우
        # 즉 num 값을 찾지 못할 시에 0을 반환해야 하므로, 처음에 -1로 설정해야 한다.

    # hi는 lst의 모든 원소가 num보다 작을 경우
        # 즉 num 값을 찾지 못할 시에 N을 반환해야 하므로, 처음에 N으로 설정해야 한다.

    # lo < o < hi, 즉 lo/hi는 항상 정답의 범위를 나타낼 수 있도록 해야 한다.
    lo, hi = -1, N
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if num > lst[mid]:
            lo = mid
        else:
            hi = mid

    return hi


def upperBound(num):
    lo, hi = -1, N
    while lo+1 < hi:
        mid = (lo + hi) // 2

        if num >= lst[mid]:
            lo = mid
        else:
            hi = mid

    return hi


N = int(input())
lst = list(map(int, input().split()))
lst.sort()

M = int(input())
have = list(map(int, input().split()))

result = [0 for i in range(M)]
for i in range(len(have)):
    lower = lowerBound(have[i])
    upper = upperBound(have[i])
    result[i] += (upper - lower)

print(*result)
