# 풀이 시간: 1시간 20분 + 37분(시간초과)
# 시간복잡도: O(최종경로길이)
# 공간복잡도: O(M*a(N) + len(dict)*K)
# 유형: union-find, dp
# 참고:
# union-find (1717, 20040)
    # https://www.acmicpc.net/source/76760622
    # https://www.acmicpc.net/source/77687636
# dp (12865)
    # https://www.acmicpc.net/source/65429288

# 시간초과 → 배낭문제를 1차원 dp로 해결
    # 시간복잡도는 똑같지만, dp 배열을 접근 속도를 더 빠르게 한다.
    # https://sskl660.tistory.com/88

import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]



def union(x, y):
    rootX = find(x)
    rootY = find(y)

    parent[rootX] = rootY


# O(M * a(N))
def solve_unionFind():
    global result
    global parent

    result = 0
    parent = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())

        if find(a) != find(b):
            union(a, b)

    # union을 진행한 후, 하위 노드에 대한 부모도 같이 변경해주기 위함.
    for i in range(1, N + 1):
        find(i)

    # value로 list를 사용하기 위해 defaultdict을 사용함
    # 같은 친구 관계에 있는 것들끼리, 집합을 만들었다.
    dicts = defaultdict(list)
    for i in range(1, N + 1):
        dicts[parent[i]].append(candy[i])

    return dicts


# O(분리집합 갯수 * 최대로 훔칠 수 있는 아이들 수)
def solve_dp():

    # i번째 집합의 j번째 사탕 갯수에서 가질 수 있는 최댓값 저장을 위한 1차원 dp 테이블을 정의한다!!
    dp = [0] * K

    for friends in dicts.values():
        w = len(friends)  # 친구 몇 명?
        v = sum(friends)  # 친구 사탕을 모두 뺏을 때 가질 수 있는 사탕은 몇 개?

        # 1차원 dp로 해결하기 위해서, 뒤에서부터 dp 값을 갱신한다.
        for j in range(K-1, w-1, -1):  # 현재 뺏을 수 있는 최대 아이들
            # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            dp[j] = max(dp[j], dp[j - w] + v)

    return dp[K-1]



# 아이들 수, 아이들의 친구 관계 수, 울음소리가 공명하기 위한 아이 수
N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))

# 친구관계를 분리 집합으로 파악
dicts = solve_unionFind()

# 4명의 아이들 집합 사탕 vs 2명의 아이들 집합 사탕 + 2명의 아이들 집합 사탕
# 어느 것이 더 많이 훔칠 수 있는지 파악해야 하므로 "배낭문제" dp를 사용한다.
result = solve_dp()

print(result)