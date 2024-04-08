# 참고 : https://www.acmicpc.net/source/74161660
# insert 최적화
    # fill_table()로 리프노드의 인덱스를 IndexTable에 초기화시킨다.
    # 이후 insert를 할 때 IndexTable에서 해당 숫자의 트리 리프노드 인덱스를 찾아낸 뒤
    # idx // 2 하여, 상위 노드들을 갱신시키는 방법으로 풀 수 있다.

import sys
input = sys.stdin.readline

def update(start, end, value, idx):
    if start == end:
        tree[idx] -= 1
        return start

    mid = (start+end) // 2
    if value <= tree[idx*2]:
        num = update(start, mid, value, idx*2)
    else:
        num = update(mid+1, end, value-tree[idx*2], idx*2+1)

    tree[idx] = tree[idx*2] + tree[idx*2+1]
    return num



def fill_table(start, end, idx):
    if start == end:
        IndexTable[start] = idx
        return

    mid = (start + end) // 2
    fill_table(start, mid, idx*2)
    fill_table(mid+1, end, idx*2+1)

IMAX = 2000000
tree = [0] * (2**22)
IndexTable = [0] * (IMAX+1)
fill_table(1, IMAX, 1)

N = int(input())
for _ in range(N):
    T, X = map(int, input().split())

    if T == 1:
        idx = IndexTable[X]
        while idx:
            tree[idx] += 1
            idx //= 2

    else:
        result = update(0, IMAX-1, X, 1) + 1
        print(result)