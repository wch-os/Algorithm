# 풀이 시간: 21분 + 34분
# 시간복잡도: [2 * O(2^k)] + [2 * O(len(k) * O(log(len(k)))]
# 공간복잡도: O(2^k)
# 유형: mitm, bns
# 참고:

# 주어진 K 값을 기준으로, upper/lowerBound를 구하고 upper - lower 로 해당 구간의 동일한 값 갯수를 파악하면 된다.

# S = 0일 때 예외를 두지 말고, 크기가 0인 부분수열은 .pop()을 하고 시작하자.
# 그리고 sumA, sumB에서 각각 S값이 있는지 확인하자.
    # sumA도 같이 정렬을 해줬어야죠.. ㅠ


# O(2^len(k))
def createPartialSum(k, sumK, l, value):
    if l == len(k):
        sumK.append(value)
        return

    createPartialSum(k, sumK, l + 1, value + k[l])  # l번째 원소 포함 o
    createPartialSum(k, sumK, l + 1, value) # l번째 원소 포함 x


# O(log(len(k)))
# lowerBound 구하기
def lowerBound(lst, criteria):
    lo, hi = -1, len(lst),

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if lst[mid] < criteria:
            lo = mid
        else:
            hi = mid

    return hi



# O(log(len(k)))
# upperBound 구하기
def upperBound(lst, criteria):
    lo, hi = -1, len(lst),

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if lst[mid] <= criteria:
            lo = mid
        else:
            hi = mid

    return hi


def minusUpperLower(sums, criteria):
    return upperBound(sums, criteria) - lowerBound(sums, criteria)



# O(len(k) * log(len(k)))
def main():
    # 정수의 갯수, 수열의 원소를 더해서 목표하는 값
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    a, b = lst[:N // 2], lst[N // 2:]
    sumA, sumB = [], []

    createPartialSum(a, sumA, 0, 0)
    createPartialSum(b, sumB, 0, 0)
    sumA.pop()
    sumB.pop()

    result = 0
    sumA.sort()
    sumB.sort()
    for one in sumA:
        # ---Bound + one = S 가 되어야 한다.
        # ---Bound = S - one 이 되어야 한다.

        result += minusUpperLower(sumB, S - one)

    result += minusUpperLower(sumA, S)
    result += minusUpperLower(sumB, S)

    print(result)



if __name__ == "__main__":
    main()