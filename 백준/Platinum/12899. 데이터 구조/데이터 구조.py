import sys
input = sys.stdin.readline

# 트리의 리프노드에는 해당 숫자가 있는지
#      상위노드에는 숫자가 있는 하위노드의 갯수가 저장되어 있다. (i번째 숫자인지 파악하기 위함)

# 트리로 데이터 구간별 개수를 파악해야 하므로
# 데이터 개수가 N개일 때, N보다 큰 가장 가까운 N의 제곱수의 2배만큼 배열의 크기를 미리 만들어야 한다.
tree = [0 for _ in range(2000000 * 4)]

# start : 시작 인덱스, end : 마지막 인덱스
# value : 기준 인덱스
# idx : insert 하면서 바뀌는 노드 인덱스(리프에서 관련 상위 노드까지)
def insert(start, end, value, idx):
    # 리프 노드 + 1
    if start == end:
        tree[idx] += 1
        return tree[idx]

    # 기준점에 따라 insert 위치를 찾기 위해, 자식 노드 탐색
    mid = (start + end) // 2
    if value <= mid:
        insert(start, mid, value, idx*2)
    if value > mid:
        insert(mid+1, end, value, idx*2+1)

    # 재귀 결과, 상위 노드도 갱신
    tree[idx] = tree[idx*2] + tree[idx*2+1]
    return tree[idx]


# start : 시작 인덱스, end : 마지막 인덱스
# idx : value 숫자의 인덱스
# value : 삭제해야 할 몇 번째 수
def update(start, end, value, idx):
    if start == end:
        tree[idx] -= 1
        return start

    # 자식 노드 탐색
    mid = (start+end) // 2
    if value <= tree[idx*2]:
        num = update(start, mid, value, idx*2)
    else:
        num = update(mid+1, end, value-tree[idx*2], idx*2+1)

    # 재귀 결과, 상위 노드도 갱신
    tree[idx] = tree[idx*2] + tree[idx*2+1]
    return num


N = int(input())
for _ in range(N):
    T, X = map(int, input().split())

    IMAX = 2000000
    if T == 1:
        # start, end, value, idx
        insert(0, IMAX-1, X-1, 1)

    elif T == 2:
        # start, end, value, idx
        result = update(0, IMAX-1, X, 1) + 1 # 리프노드에서 0번째 노드와 1을 매핑 시켰으므로, +1 을 한다.
        print(result)