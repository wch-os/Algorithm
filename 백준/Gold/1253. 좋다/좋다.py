# 풀이 시간 : 30분 + 10분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 참고 : -

# 투포인터는 mid 값을 쓰는 것이 아니라, lo += 1 / hi -= 1
# 자기 자신 값 제외
# 직전 코드와 차이점은?
    # 초기 lo, hi에서부터 k와 같을 수도 있다.
    # lo, hi 모두 k와 비교 후 조정한다 하더라도 lo, hi 인덱스가 같아질 우려가 있으므로,
        # sumK == lst[k] 일 때 lo, hi가 k 인덱스인지 확인 후 조정이 필요하다.

# k번째 있는 수가 좋은 수인지 투포인터 체크
def twoPointer(k):
    # 0 ~ N-1번째 수로 lst[k] 숫자를 표현해야 된다.
    lo, hi = 0, N - 1

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