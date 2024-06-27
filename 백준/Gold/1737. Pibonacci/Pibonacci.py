# 풀이 시간: 15분
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: dp, dict
# 참고: -

import math
from collections import defaultdict

def solve(n):
    if 0 <= n <= math.pi:
        return 1

    if dicts[n]:
        return dicts[n]

    dicts[n] = (solve(n-1) + solve(n - math.pi)) % 1000000000000000000
    return dicts[n]


N = int(input())
dicts = defaultdict(list)

print(solve(N))
