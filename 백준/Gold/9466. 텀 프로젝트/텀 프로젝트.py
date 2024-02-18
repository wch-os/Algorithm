# 풀이 시간 : 20분 + 40분
# 시간복잡도 : O(bfs)
# 공간복잡도 : O(N)
# 참고 : https://aia1235.tistory.com/47

# 자기자신 or 사이클 형성이 되야 한 팀
# 사이클이 있는지 판단해야 함

# 탐색할 때마다 visited 초기화
# → 1번만 초기화, 사이클 노드 visited = True (그대로 유지)
# → 사이클 노드가 아닐 때 visited = False 를 추가하지 않음..

# 기존 코드에서 사이클 노드가 아닐 때 visited = False 처리하는 부분이 시간이 오래 걸렸을 것이라 생각된다.

# RecursionError → sys.setrecursionlimit(10**6)

import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result

    visited[x] = True
    cycle_list.append(x)

    # x가 팀을 하고자 하는 사람
    select = want[x]

    # 다음에 갈 노드를 이미 방문한 경우
    if visited[select]:
        # 다음에 갈 노드가 cycle_list에 있는 경우
        if select in cycle_list:
            result -= len(cycle_list[cycle_list.index(select):])
        return

    # 미방문 노드일 경우
    else:
        dfs(want[x])



T = int(input())
for _ in range(T):
    N = int(input()) # 학생 수
    want = [0] + list(map(int, input().split())) # 각자 지목

    notTeam = 0
    visited = [False for _ in range(N+1)]

    result = N
    for i in range(1, N+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)

    print(result)