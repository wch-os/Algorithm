# 풀이 시간 : 15분
# 시간복잡도 : O(NM)
# 공간복잡도 : O(N or M)
# 참고 : -

# 이분탐색 문제인가..?
    # 적절한 칭호를 빨리 찾는 이분탐색 문제였네.. ㅎㅎ

# lower_bound인 이유 : 기준 power가 포함된 범위 내의 칭호를 붙여주는 것이다. 초과가 아닌

import sys
input = sys.stdin.readline

def search(power, start, end):
    while start < end:
        mid = (start + end) // 2

        if power > int(cri[mid][1]):
            start = mid + 1

        else:
            end = mid

    return end



N, M = map(int, input().split())

cri = []
for _ in range(N):
    name, limit = map(str, input().split())
    cri.append((name, limit))

powers = [int(input()) for _ in range(M)]


for p in powers:
    idx = search(p, 0, len(cri)-1)

    print(cri[idx][0])