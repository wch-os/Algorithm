# 풀이 시간 : 30분
# 시간복잡도 : O(NlogN)
# 공간복잡도 : O(N)
# 참고 : -

# 문제가 무슨 말인가 했네..
# 어치파 사이클이 형성된다.

def dfs(start):
    for k in graph[start]:
        if not visited[k]:
            visited[k] = True
            return dfs(k)



T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i].append(lst[i])

    visited = [False] * (N + 1)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            cnt += 1

    print(cnt)