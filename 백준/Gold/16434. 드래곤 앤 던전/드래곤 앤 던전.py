# 풀이 시간 : 14분 + 5분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 참고 : -

# 1번째 틀린 코드 수정

# 각 방을 차례대로 돌파한다.
    # t = 1, 방에서 몬스터에게 맞은 데미지를 계산한다.
    # t = 2, 포션을 더할 때 최대 체력을 넘지 않도록 주의한다.
    # 용사가 살아남기 위해 + 1을 한다.

    # !!. 후반부에 포션이 있는 방밖에 없어, hp 계산이 틀릴 수도 있으므로 몬스터를 만날 때마다 필요한 최소 hp를 갱신시켜 주어야 한다.

import sys
input = sys.stdin.readline

# t, a, h
# t: 1, 공격력: a, 생명력:h 인 몬스터
# t: 2, 공격력: a, 생명력:h 인 포션
N, attack = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]

result = 0
hp = 0
for [t, a, h] in rooms:
    if t == 1:
        monsterAttack = (h - 1) // attack
        hp -= (monsterAttack * a)
        result = min(result, hp)

    else:
        attack += a
        hp += h
        if hp > 0:
            hp = 0

print(-result + 1)