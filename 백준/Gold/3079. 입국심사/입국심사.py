# 풀이 시간 : 1시간
# 시간복잡도 : O(N*log(10^18) = 60N)
    # 정점 수 + 간선 수
    # dfs 깊이가 5가 되면 바로 탈출하기 때문에 N + M 복잡도로 생각했다.
# 공간복잡도 : O(N)
# 참고 : -

import sys
input = sys.stdin.readline

# mid초 이내에 모든 사람이 입국 심사대를 통과할 수 있는가?
def check(mid):
    count = 0
    for room in rooms:
        count += mid // room # 각 심사대가 mid초 동안 심사할 수 있는 사람
        if count >= M: # 모두 통과 가능
            return True

    return False


def bns():
    # check(lo): 0초 이내로 통과 불가, False
    # check(hi): 입력값 최대 범위 시간 이내로 통과 가능, True
    lo, hi = 0, 10**18

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if not check(mid):
            lo = mid
        else:
            hi = mid

    return hi


N, M = map(int, input().split())
rooms = [int(input()) for _ in range(N)]

print(bns())