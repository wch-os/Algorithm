# 풀이 시간 : 35분 + 40분(dp) + 30분
# 시간복잡도 : O(1)
# 공간복잡도 : O(1)
# 참고 : https://kiffblog.tistory.com/181

# 1
# ---------
# 1, 1
# 1, 1, 1
# 1, 2, 1 = 4
# ---------
# 1, 2, 1, 1
# 1, 2, 2, 1 → 6
# 1, 2, 2, 1, 1
# 1, 2, 2, 2, 1
# 1, 2, 3, 2, 1 = 9
# ---------
# 1, 2, 3, 2, 1, 1

# 홀수(2n-1)번 이동할 때, 최대이동거리는 "n^2" 이다.
    # n(n+1)/2 * 2 - n = n^2
# 짝수(2n)번 이동할 때, 최대이동거리는 "n^2+n" 이다.
    # n(n+1)/2 * 2 = n^2 + n

import math

def solve(move):
    sqrtMove = int(math.sqrt(move))

    if move == (sqrtMove ** 2):
        n = 2 * sqrtMove - 1

    elif sqrtMove ** 2 < move <= sqrtMove * (sqrtMove + 1):
        n = 2 * sqrtMove

    else:
        n = 2 * sqrtMove + 1

    return n



T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    move = y-x # 총 이동 거리

    print(solve(move))