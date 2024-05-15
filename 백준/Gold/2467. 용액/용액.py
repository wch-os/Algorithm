# 풀이 시간 : 19분 + 20분
# 시간복잡도 : O(N * log(N))
# 공간복잡도 : O(N)
# 참고 : -

def bns():
    lo, hi = 0, N - 1
    result = abs(lst[lo] + lst[hi])
    resultX, resultY = lst[lo], lst[hi]

    while lo + 1 <= hi:
        mid = lst[lo] + lst[hi]

        # 두 용액 최솟값 갱신
        if result >= abs(mid):
            result = abs(mid)
            resultX, resultY = lst[lo], lst[hi]

        # 투 포인터
        if mid < 0:
            lo += 1
        else:
            hi -= 1

    return resultX, resultY



N = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(*bns())