# 풀이 시간 : 30분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 참고 : -

# 투포인터는 mid 값을 쓰는 것이 아니라, lo += 1 / hi -= 1
# 자기 자신 값 제외
# 직전 코드와 차이점은?

# k번째 있는 수가 좋은 수인지 투포인터 체크
def twoPointer(k):
    # 0 ~ k-1번째 수로 lst[k] 숫자를 표현해야 된다.
    lo, hi = 0, len(lst) - 1

    # lo + 1 == hi 도 검사 필요
    while lo < hi:
        sumK = (lst[lo] + lst[hi])

        if sumK == lst[k]:
            if lo == k: lo += 1
            elif hi == k: hi -= 1
            else:
                return True

        # 합이 더 작을 경우
        elif sumK < lst[k]:
            lo += 1

        else:
            hi -= 1


    return False



N = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = 0
for i in range(len(lst)):
    if twoPointer(i):
        result += 1

print(result)