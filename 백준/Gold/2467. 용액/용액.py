# 풀이 시간 : 19분 + 20분
# 시간복잡도 : O(N * log(N))
# 공간복잡도 : O(N)
# 참고 : -

# 출력값 정렬

def lowerBound(tmp):
    lo, hi = 0, N-1

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if tmp > lst[mid]:
            lo = mid
        else:
            hi = mid

    return hi


N = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = float('inf')
for i in range(N):
    # lowerBound 이므로 abs(lst[i]) 이상 값 인덱스가 나온다.
    idx = lowerBound(abs(lst[i]))

    # lowerBound 직전 인덱스도 체크 (idx-1, idx)
    for j in range(idx-1, idx+1):
        if i == j: # 같은 용액은 배제
            continue

        num = abs(lst[i] + lst[j])
        if result >= num:
            result = num
            resultX, resultY = lst[i], lst[j]

print(*sorted((resultX, resultY)))
