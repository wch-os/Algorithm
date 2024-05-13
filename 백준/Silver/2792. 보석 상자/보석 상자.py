import sys
input = sys.stdin.readline

# 결정 문제: mid 개수로 나눠주었을 때,
# 항상 같은 색상의 보석만 가져간다는 규칙 하에 N 이하인 사람들에게 나눠주고 있는가? → True
# 아니면 더 많은 사람에게 나눠줘야 하는가? → Fasle
def check(mid):
    person = 0
    for m in mlist:
        # 'mid-1'은 나머지 보석 개수도 나눠줘야 하므로
        person += (m + mid-1) // mid 

    return person <= N


def bns():
    # CheckList
    # 1. Check(lo) != Check(hi)를 만족하는가?
    # Check(0) = True, Check(max(mlist)) = True 이다.
    # 2. lo는 정답이 될 수 있는 모든 범위를 나타낼 수 있는가?
    # 1부터 정답이 가능하다.
    lo, hi = 0, max(mlist)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        # check(low) == check(mid), False
        if not check(mid):
            lo = mid
        else:
            hi = mid

    # lo: False, hi: True
    # 문제에서 원하는 답은 True이면서, mid 개수가 가장 적게(질투심이 최소가 되게) 보석을 나눠주어야 한다.
    return hi


N, M = map(int, input().split())
mlist = [int(input()) for _ in range(M)]

print(bns())