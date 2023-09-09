N = int(input())
children = list(map(int, input().split()))

inSet = set()
cq = {key: 0 for key in range(1, N+1)}
for child in children:
    # 그 다음 숫자가 set에 있으면
    if child+1 in inSet:
        cq[child+1] = cq[child]

    # 없으면 (연속된 숫자가 그 뒤 인덱스에 있다는 것)
    else:
        cq[child+1] = cq[child] + 1

# 가장 큰 value, 즉 가장 길게 연속된 횟수를 찾기
cqMax = max(cq.values())

# 연속된 숫자를 제외한 N-cqMax 번 재배열하면 된다.
print(N-cqMax)
