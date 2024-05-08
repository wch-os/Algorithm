# 풀이 시간 : 15분 + 18분
# 시간복잡도 : O(N+M)
    # 정점 수 + 간선 수
    # dfs 깊이가 5가 되면 바로 탈출하기 때문에 N + M 복잡도로 생각했다.
# 공간복잡도 : O(N)
# 참고 : -

# 재귀가 False로 끝났을 때 분기 재귀를 체크하지 않았다.
    # ex. 예제 2번을 디버깅하면 0번에서 바로 True가 나와야 한다.

def dfs(num, depth):
    global visited, flag

    if depth == 5:
        return True

    for k in lst[num]:
        if not visited[k]:
            visited[k] = True
            if dfs(k, depth + 1):
                return True
            visited[k] = False

    return False


def judge():
    global visited

    for i in range(N):
        visited = [False for _ in range(N)]
        visited[i] = True
        if dfs(i, 1):
            return True

    return False


N, M = map(int, input().split())

lst = list([] for _ in range(N))
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

if judge():
    print(1)
else:
    print(0)
