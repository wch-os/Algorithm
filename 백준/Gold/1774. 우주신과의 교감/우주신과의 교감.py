import math
import sys
input = sys.stdin.readline

def calDistance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 )

def find(a):
    if parents[a] == a:
        return a

    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    parents[rootA] = rootB


if __name__ == "__main__":
    N, M = map(int, input().split()) # 우주신 개수, 이미 연결된 신들과의 통로 개수
    location = [list(map(int, input().split())) for _ in range(N)] # 우주신 위치
    connect = [list(map(int, input().split())) for _ in range(M)] # 이미 연결된 통로

    dis = [] # 각 신들의 거리
    for i in range(N):
        for j in range(i + 1, N):
            dis.append((calDistance(location[i], location[j]), i + 1, j + 1))

    dis.sort()
    result = 0
    parents = [0] + [i for i in range(1, N + 1)]

    """이미 연결된 통로"""
    for a, b in connect:
        if find(a) != find(b):
            union(a, b)

    """MST - 최소 비용으로 노드 연결"""
    for cost, a, b in dis:
        if find(a) != find(b):
            union(a, b)
            result += cost

print("{:.2f}".format(result))
