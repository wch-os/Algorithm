# 풀이 시간 : 1시간
# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n)
# 참고 : -

# core : 제일 작은 2개가, 제일 큰 것보다 커야 함
# 1. 그러면 제일 작은 2개의 숫자를 먼저 선택하자. (연속된 수)
# 2. 삼각형 조건을 만족하는 수를 count

def solve(a, b):
    sumAB = a + b
    maxAB = max(a, b)

    if a == b:
        count = 0
    else:
        count = 1

    for i in lst:
        # 삼각형 조건 만족
        # i는 가장 긴 변이어야 함
        if maxAB <= i < sumAB:
            count += 1

    return count


N = int(input())
lst = list(map(int, input().split()))
lst.sort()

if N == 2:
    print(2)
elif N == 1:
    print(1)
else:
    long = 0
    for i in range(len(lst)-1):
        result = solve(lst[i], lst[i+1])
        if long < result:
            long = result

    print(long)