# 풀이 시간: n시간
# 시간복잡도: O(V+E)
# 공간복잡도: O(V+E)
# 유형: SCC(Strongly Connected Component)
# 참고:
# 1) https://blog.naver.com/ndb796/221236952158
# 2) https://velog.io/@cldhfleks2/Strongly-Connected-Component
# 3) https://yjg-lab.tistory.com/188
# 4) https://yiyj1030.tistory.com/493#google_vignette (예시가, 잘 설명되어 있음)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def tarjan():
    def dfs(now):
        nonlocal id_counter

        id_counter += 1
        ids[now] = low_link[now] = id_counter

        stack.append(now)
        on_stack[now] = True

        for next in graph[now]:

            # 방문하지 않은 노드라면
            if ids[next] == 0:
                dfs(next)
                low_link[now] = min(low_link[now], low_link[next])

            # 스택에 있는 노드라면
            elif on_stack[next]:
                low_link[now] = min(low_link[now], ids[next])


        if ids[now] == low_link[now]:
            scc = []
            while True:
                top = stack.pop()
                on_stack[top] = False
                scc.append(top)

                if top == now:
                    break

            scc.sort()  # 정점 번호 오름차순 정렬
            SCC.append(scc)


    id_counter = 0
    ids = [0] * (V + 1)  # 노드별 방문 순서
    low_link = [0] * (V + 1)  # 도달 가능한 가장 낮은 id

    stack = []  # dfs 스택
    on_stack = [False] * (V + 1)

    SCC = []  # SCC 저장 리스트

    """ 모든 노드에 대해 DFS 수행 """
    for i in range(1, V + 1):
        if ids[i] == 0:
            dfs(i)

    SCC.sort(key=lambda x: x[0])
    return SCC



# 입력 처리
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

# SCC 찾기
result = tarjan()

# 출력
print(len(result)) # SCC 개수
for scc in result:
    print(*scc, -1)
