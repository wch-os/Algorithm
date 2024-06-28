# 풀이 시간: 17분
# 시간복잡도: O(N^2)
# 공간복잡도: O(N^2)
# 유형: union-find
# 참고: https://ca.ramel.be/100

import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    rootX = find(x)
    rootY = find(y)

    parents[rootX] = rootY


def possible():
    # 부모노드가 바뀌고, 갱신이 안되었을 수도 있으므로 find()를 1번씩 호출해준다.
    for i in range(1, N + 1):
        find(i)

    # 여행 계획의 모든 노드가 같은 집합에 있는지 확인한다.
    center = parents[travel[0]]
    for t in travel:
        if center != parents[t]:
            return "NO"

    return "YES"


N = int(input()) # 도시의 수
M = int(input()) # 여행 계획에 속한 도시의 수

board = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N+1)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            union(i+1, j+1)

travel = list(map(int, input().split()))
print(possible())
print()