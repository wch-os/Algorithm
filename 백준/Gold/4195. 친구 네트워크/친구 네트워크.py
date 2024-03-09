# 풀이 시간 : 1시간
# 시간복잡도 : O(M * a(N))
    # M : 연산 개수
    # a(N) : 역 Ackermann 함수로, 경로 압축을 하는 경우 find()는 N의 증가에 따라서 매우 느리게 증가한다.
        # 실제로 모든 n에 대해서 5보다 작은 값으로 수렴한다..
# 공간복잡도 : O(N)
# 참고 : https://reliablecho-programming.tistory.com/81

# 접근법
    # 문자열 유니온 파인드
    # 일단 parent = dict() 을 만든다.
    # A, B 가 person에 속한다면 생성 X, 속하지 않는다면 생성, 이 때 생성 인덱스와 같게 한다.
        # ex. parent[A] = A
        # ex. parent[B] = B
        # ex. parent[C] = C
    # A, B의 부모를 find() 한다.
    # union() 하여 집합 value 값으로 집합화 한다.

# 생각
    # 집합의 개수를 어떻게 구해야 하는지에서 생각이 떠오르지 않아 블로그를 참고했다.

    # 이전 유니온 파인드에서는 rootX, rootB의 대소 관계에 따라서 부모를 지정해주었다.
    # 하지만 참고한 블로그에서는 root가 틀린 경우 무작위로 부모를 설정해주었다.
    # 곰곰히 생각해보면 대소 관계에 따라서 트리를 구성하면 최적화 되지만, 부모-자식을 어떻게 맺든 상관은 없었다.

import sys
input = sys.stdin.readline

T = int(input())
def find(k):
    if parent[k] == k:
        return k

    parent[k] = find(parent[k]) # 부모 갱신, 경로 압축 최적화
    return parent[k]


def union(a, b):
    rootA = find(a) # a 원소의 최상위 루트 값
    rootB = find(b) # b 원소의 최상위 루트 값

    if rootA != rootB:
        parent[rootB] = rootA # B가 A의 하위로 들어감
        number[rootA] += number[rootB] # A 원소 개수 늘어나기

    print(number[rootA])


for _ in range(T):
    parent = dict() # (name, parent node) 저장
    number = dict() # (rootK, cnt) / 루트 원소의 집합의 개수 파악

    F = int(input()) # 친구 관계의 수

    # 친구 관계는 두 사용자의 아이디로 이루어져 있다.
    for z in range(F):
        A, B = map(str, input().split())

        # 새로운 이름이면 parent 에 추과
        # 초기 parent는 자기 자신
        if A not in parent:
            parent[A] = A
            number[A] = 1
            
        if B not in parent:
            parent[B] = B
            number[B] = 1

        union(A, B)