# 틀렸던 이유
    # 1)
        # 시작 지점에 관계없이 음의 사이클이 존재하는지만 판단 문제이므로, 시작 지점은 아무데나 두면 된다.
        # 즉, dis[start] != INF 조건을 삭제해줘야 한다.

# dis[start] != INF 의미
            # start 시작지점으로부터 이어진 노드의 최소 거리를 구하기 위함.
            # 그러니까 특정 노드를 시작으로 타 노드까지의 최소 거리를 구하는 알고리즘이다.

            # 그런데 이 문제에서는, 시작점에 관계없이 음의 사이클 유무를 판단해야 한다.

    # 2)
        # float('inf') 에서 음수 가중치를 더해주어도 그대로 무한대이다.
        # 즉, 현재값과 이전 값이 비교가 되지 않는다...

    # 3)
        # 도로는 연결된 지점이므로, 양방향
        # 웜홀은 풀었던대로 단방향


# 풀이 시간 : 2시간
# 시간복잡도 : O(V(M+W)
# 공간복잡도 : O(N) or O(M+W)
# 참고 :
    # 개념 숙지 - https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm
    #         - https://great-park.tistory.com/134
    # 다른 문제 - https://www.acmicpc.net/source/65172892
    # 틀린 이유 - https://letalearns.tistory.com/78
    #         - https://backtony.github.io/algorithm/2021-02-13-algorithm-boj-class4-10/

import sys
input = sys.stdin.readline

def bellmanFord(start):
    # 시작 노드 초기화
    # 본인 지점까지 가는데 필요 최소 시간은 '0'
    minDis[start] = 0

    # 음의 사이클이 없고 정점이 V개인 그래프에서
    # 한 정점에서 출발한 다른 정점까지의 최단경로는, 많아봐야 V-1개의 간선을 지난다.
    # 즉, 한 번 지난 정점은 다시 지나지 않는다.
    for i in range(V):
        # 모든 간선에 대해 탐색
        for start, end, cost in graph:
            # if minDis[start] != float('inf'):
            # 최적화 루트(음의 간선)가 있다면, 갱신을 해 준다.
            if minDis[end] > minDis[start] + cost:
                minDis[end] = minDis[start] + cost

                # 마지막 V번째에서도 값이 갱신된다면, 음수 순환이 존재
                if i == V - 1:
                    return True

    return False



TC = int(input()) # 테스트케이스 개수

for _ in range(TC):
    # V : 지점의 수 / M : 도로의 개수 / W : 웜홀의 개수
    V, M, W = map(int, input().split())

    # 간선, 즉 도로 + 웜홀의 정보를 담는 리스트
    # 간선(출발지, 목적지, 비용)
    graph = []
    # minDis[i] 지점까지 가는데 최소 필요 시간
    minDis = [10001] * (V+1)

    for _ in range(M):
        # S, E : 연결된 지점의 번호 / T : 도로를 통해 이동하는데 걸리는 시간
        S, E, T = map(int, input().split())
        graph.append((S, E, T))
        graph.append((E, S, T)) # 연결된 지점. 양방향

    for _ in range(W):
        # s, e : 시작, 도착 지점 / t : 줄어드는 시간
        s, e, t = map(int, input().split())
        graph.append((s, e, -t)) # 줄어드는 시간이므로, -t


    negative_cycle = bellmanFord(1)

    # 음의 사이클이 있다면,
    # 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하다.
    if negative_cycle:
        print("YES")

    # 음의 사이클이 없다면,
    # 불가능하다.
    else:
        print("NO")