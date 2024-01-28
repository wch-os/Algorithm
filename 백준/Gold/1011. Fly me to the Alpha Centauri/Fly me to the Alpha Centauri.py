# 풀이 시간 : 35분 + 40분(dp) + 30분
# 시간복잡도 : O(1)
# 공간복잡도 : O(1)
# 참고 : https://kiffblog.tistory.com/181
#       https://st-lab.tistory.com/79 (잘 설명됨)

# 1
# ---------
# 1, 1
# 1, 1, 1
# 1, 2, 1 = 4 (3번 이동 : 홀수 경계값)
# ---------
# 1, 2, 1, 1 (4번 이동)
# 1, 2, 2, 1 → 6 (4번 이동 : 짝수 경계값)

# 1, 2, 2, 1, 1 (5번 이동)
# 1, 2, 2, 2, 1 (5번 이동)
# 1, 2, 3, 2, 1 = 9 (5번 이동 : 홀수 경계값)
# ---------
# 1, 2, 3, 2, 1, 1

# 홀수(2n-1)번 이동할 때, 최대이동거리는 "n^2" 이다.
    # n(n+1)/2 * 2 - n = n^2
# 짝수(2n)번 이동할 때, 최대이동거리는 "n^2+n" 이다.
    # n(n+1)/2 * 2 = n^2 + n

import math

def solve(move):
    sqrtMove = int(math.sqrt(move))

    # 홀수번일 때 최대이동거리만큼 이동해야 하므로
    # 2 * n -1
    if move == (sqrtMove ** 2):
        n = 2 * sqrtMove - 1

    # 위의 조건보다 크고, 짝수번 경계값 사이일 때
    # 2 * n
    elif sqrtMove ** 2 < move <= sqrtMove * (sqrtMove + 1):
        n = 2 * sqrtMove

    # 이 외의 경우, 나머지(홀수 경계값 move가 제곱수가 되기 직전)
    # 2 * n + 1
    else:
        n = 2 * sqrtMove + 1

    return n



T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    move = y-x # 총 이동 거리

    print(solve(move))
