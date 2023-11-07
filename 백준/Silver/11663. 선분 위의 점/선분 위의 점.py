# 풀이 시간 : 1시간
# 시간복잡도 : O(2MlogN)
# 공간복잡도 : O(N or M)
# 참고 : -

# 1. 점들을 먼저 오름차순 정렬한다.
# 2. 각 선분의 시작점(upper)과 끝점(lower)의 index를 찾는다
# 3. 해당 index 범위 내의 dot 개수를 구한다.

# lower, upper bound 문제는 빠르게 이해함.
# 그러나 하나의 함수로 통일하고, 후처리 하는 과정에서 시간을 소모했다.. (결국 따로 메소드 만듦)

import sys
input = sys.stdin.readline

# lower_bound
def lower_search(lineS):
    left, right = 0, N

    while left < right:
        # 선분의 중앙점
        mid = (left + right) // 2

        if dots[mid] < lineS:
            left = mid + 1

        else:
            right = mid

    return right


# upper_bound
def upper_search(lineS):
    left, right = 0, N

    while left < right:
        # 선분의 중앙점
        mid = (left + right) // 2

        if dots[mid] <= lineS:
            left = mid + 1

        else:
            right = mid

    return right


N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

line = [list(map(int, input().split())) for _ in range(M)]

for s, e in line:
    # 선분의 시작점을 기준으로, lower_bound
        # 즉, "s 이상의 최소 인덱스"를 찾는다.
    indexS = lower_search(s)

    # 선분의 끝점을 기준으로, upper_bound
        # 즉, "e 초과의 최소 인덱스"를 찾는다.
    indexE = upper_search(e)

    print(indexE - indexS)