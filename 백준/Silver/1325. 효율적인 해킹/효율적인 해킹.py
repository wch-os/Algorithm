# 풀이 시간 : 15분
# 시간복잡도 : O(N+e)
# 공간복잡도 : O(N+e)
# 참고 : -
    # Python3는 시간초과
    
from collections import deque

def bfs(k):
    visited = [False] * (N + 1) # 계속 초기화 필요
    cnt = 0 # 연결된 간선 갯수 세기

    q = deque()
    q.append(k)
    visited[k] = True

    while q:
        x = q.popleft()

        for one in graph[x]:
            if not visited[one]: # 미방문 간선
                cnt += 1
                visited[one] = True
                q.append(one)

    return cnt


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    #"B를 해킹하면, A도 해킹할 수 있다."
    #graph[a].append(b)
    graph[b].append(a)

computer = []
for i in range(1, N+1):
    computer.append([i, bfs(i)])

computer.sort(key = lambda x : -x[1]) # 간선이 가장 많이 연결된 컴퓨터 번호로, 내림차순 정렬

result = []
hackNum = computer[0][1] # 가장 많이 연결된 컴퓨터 번호
for a, b in computer:
    if hackNum == b:
        result.append(a)

print(*result)