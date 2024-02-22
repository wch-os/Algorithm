# 풀이 시간 : 50분 + 30분
# 시간복잡도 : O(V+E)
# 공간복잡도 : O(N)
# 참고 : https://ji-gwang.tistory.com/293

# 재귀 깊이 설정

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(start, idx):
    visited[start] = idx

    for k in graph[start]:
        # 인접 노드는 다른 "표식"
        if not visited[k]:
            judge = dfs(k, -idx)

            # dfs 탐색 중에 인접 노드와 같은 "표식"이 있다면
            if not judge:
                return False

        # 인접 노드와 같은 "표식"이라면
        if visited[k] == visited[start]:
            return False

    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e) # 양방향 연결
        graph[e].append(s)

    for i in range(1, V):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    if result:
        print("YES")
    else:
        print("NO")