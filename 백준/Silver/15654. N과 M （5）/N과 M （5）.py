def dfs():
    # 원하는 길이가 된다면, 결과 리스트에 해당 길이 리스트 추가
    if len(per) ==  M:
        result.append(per.copy())
        return

    for i in range(0, N):
        # lst[i]의 똑같은 원소가 있는지 판단
        if lst[i] not in per:
            per.append(lst[i])
            dfs()
            per.pop()



per = []
result = []

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 오름차순 정렬
lst.sort()

dfs()

for r in result:
    print(' '.join(map(str, r)))