def init(start, end, idx):
    if start == end:
        tree[idx] += 1
        return

    mid = (start+end) // 2
    init(start, mid, idx*2)
    init(mid+1, end, idx*2+1)
    tree[idx] = tree[idx*2] + tree[idx*2+1]


def delete(start, end, K, idx):
    if start == end:
        tree[idx] -= 1
        return start

    mid = (start+end) // 2
    if K <= tree[idx*2]:
        ret = delete(start, mid, K, idx*2)
    else:
        ret = delete(mid+1, end, K-tree[idx*2], idx*2+1)

    tree[idx] = tree[idx*2] + tree[idx*2+1]
    return ret



N, K = map(int, input().split())
tree = [0] * (N*4)

num_list = []
for i in range(1, N+1):
    num_list.append(i)


init(0, N-1, 1)


result = [delete(0, N - 1, K, 1) + 1] # 처음 K번째
cur = K
length = N-1
while length:
    rank = (cur + (K-1)) % length # delete 된 수가 있으므로 +K-1 번째 수
    if rank == 0: rank = length # 마지막 수
    numIdx = delete(0, N-1, rank, 1)
    result.append(numIdx+1) # 리프노드는 0부터 매칭되므로 +1

    length -= 1 # delete 되었으므로
    cur = rank # 현재 cursor 위치


print("<", end='')
print(*result, sep=', ', end='')
print(">")