# 풀이 시간 : 14분 + 15분
# 시간복잡도 : O(N * log(N*10^12)
# 공간복잡도 : O(N)
# 참고 : -

# 이분 탐색으로 접근해보자.
# 문제에서 요구하는 것은 '던전을 돌파하기 위한 최소 hp'이다.
# hp를 범위로 설정하고, 결정 문제를 'mid의 체력으로 던전을 통과할 수 있는가?'로 정한다.

# 유의할 점은 범위이다.
# 유저의 공격력이 1, 몬스터의 체력이 10^6 일 때 10^6-1번 맞게 된다.
# 그러한 방이 N개 있으며, 몬스터의 최대 공격력 또한 10^6이니
# (방의 개수) * (몬스터의 최대 공격력) * (1개의 방에서 최대로 맞게 되는 경우의 수)
# 무조건 통과할 수 있는 hp, hi를 N * 10^12 로 설정한다.


import sys
input = sys.stdin.readline

# mid의 체력으로 던전을 통과할 수 있는가?
def check(mid, attack):
    initHp = mid

    for [t, a, h] in rooms:
        if t == 1:
            monsterAttack = (h - 1) // attack
            mid -= (monsterAttack * a)

            if mid <= 0:
                return False


        elif t == 2:
            attack += a
            mid += h
            if mid > initHp:
                mid = initHp

    return True


def bns():
    # check(lo): 0의 체력으로 던전을 통과할 수 없다. | False
    # check(hi):  hi의 체력으로 던전을 통과할 수 있다. | True
    lo, hi = 0, N * 10 ** 12

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if not check(mid, attack):
            lo = mid

        else:
            hi = mid

    return hi


# t, a, h
# t: 1, 공격력: a, 생명력:h 인 몬스터
# t: 2, 공격력: a, 생명력:h 인 포션
N, attack = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

print(bns())