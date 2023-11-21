# 풀이 시간 : 50분 + 30분
# 시간복잡도 : O((N+M)*log(max(weight)))
# 공간복잡도 : O(N)
# 참고 : https://jie0025.tistory.com/212

# 69514622 코드에서 lower_bound 구현만 다르게 했다.

# 그래프 탐색으로 푸는건가..??
# 이렇게 풀면 왜 틀리는건가?
    # 감당 가능한 무게가 작은 쓸데없는 다리가 있을 경우,
    # 목적지까지 갈 수 있음에도 판단하지 못한다.

# 31번째 라인 부등호 반대로 함.. (감당 가능하려면, 그보다 커야지요)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    visited = [False] * (N+1)
    q = deque()
    q.append(endA)

    while len(q) > 0:
        dot = q.popleft()
        visited[dot] = True

        if dot == endB:
            return True

        for b, c in bridge[dot]:
            # 다음 목적지가 아직 방문하지 않은 '섬'일 경우 & 감당가능한 '다리'일 경우
            if not visited[b] and c >= mid:
                visited[b] = True # 큐에 계속 들어와지는 걸 막기 위해
                q.append(b)

    return False


def search(start, end):
    while start <= end:
        mid = (start + end) // 2

        # 다리들이 현재 mid 무게를 감당 가능하면, 더 중량을 올려도 됨
        if bfs(mid):
            start = mid + 1

        # 감당 불가능하면
        else:
            end = mid - 1

    return end

# N : N개의 섬,
N, M = map(int, input().split())

bridge = [[] for _ in range(N+1)]
weight = [] # 각 다리가 버틸 수 있는 무게 집합

for _ in range(M):
    a, b, c = map(int, input().split())

    bridge[a].append((b, c))
    bridge[b].append((a, c))
    weight.append(c)

endA, endB = map(int, input().split())

# 무게 최소, 최대
print(search(1, max(weight)))