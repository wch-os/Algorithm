# 참고 : https://tussle.tistory.com/1102

def insert(start, end, value, idx):
    if start == end:
        tree[idx] += 1
        return start # 이후 [start+1:] 구간 탐색을 위해, 리프노드 인덱스 return

    mid = (start+end) // 2
    if value <= mid:
        res = insert(start, mid, value, idx*2)
    else:
        res = insert(mid+1, end, value, idx*2+1)

    tree[idx] = tree[idx*2] + tree[idx*2+1]
    return res


def search(s, e, l, r, idx):
    # 범위 바깥
    if e < l or r < s:
        return 0

    # 범위 안
    if l <= s and e <= r:
        return tree[idx]

    mid = (s+e) // 2
    return search(s, mid, l, r, idx*2) + search(mid+1, e, l, r, idx*2+1)



N = int(input())
lst = list(map(int, input().split()))
lst = [[value, index] for index, value in enumerate(lst)]
lst = sorted(lst, key=lambda x:x[0])

# lst 입력값 범위대로 트리에 표현할 수가 없음 |num| <= 10억
# 따라서 정렬 후, 작은값부터 차례대로 tree[입력순서]에 삽입한다.
# 그리고 tree[입력순서+1:] 구간의 값이 있는지 확인한다.
    # 해당 구간 값의 의미는 '먼저 삽입된 현재 값보다 작은값의 갯수' swap이 필요하다.
lst.sort()

tree = [0] * (4*N)

# [3, 2, 1, 4]
result = 0
for l, i in lst:
    # 가장 처음 들어온 e, 즉 3은 tree[0]에 삽입된다.
    # 가장 작은 e, 즉 1은 tree[2]에 삽입된다.
    left = insert(0, N-1, i, 1)

    # l 원소보다 큰 원소가 몇 개가 있는지 구간합
    result += search(0, N-1, left+1, N-1, 1)

print(result)