# 원하는 조건을 만족하지 못했음에도, return을 진행했다.
# +. 원하는 조건을 만족해도, 그 다음 원소들의 합으로 S가 만들어질 수 있으므로 return을 하면 안된다.

N, S = map(int, input().split())

lst = list(map(int, input().split()))

result = []
count = 0 # 합이 S가 되는 부분수열의 개수
def dfs(start):
    global count

    # 부분수열의 크기가 양수이면 Stop 한다.
    if len(result) >= 1:
        # 수열의 원소의 합이 S가 되는 경우의 수를 찾으면 return 한다.
        if sum(result) == S:
            count += 1
        # 못 찾은 경우일 시, 계속 추가해서 백트래킹 해야한다.
        # 결과를 찾지 못해도 return을 할 경우, 해당 원소를 배제하게 된다.


    for i in range(start, len(lst)):
        result.append(lst[i])
        dfs(i+1)
        result.pop()

dfs(0)

print(count)