# 풀이 시간: 35분 + 1시간(고민,,)
# 시간복잡도: O(NlogN)
# 공간복잡도: O(N)
# 유형: priority queue
# 참고: -
# 생각:

"""
이전 코드 실패 테스트케이스
'1 2 3 4 5 6 7 8 9 10'를 갖는 최소힙/최대힙 구조에서
최소힙에서 1~4 pop, 최대힙에서 6~10 pop 이후
새롭게 2,3 insert (inserCnt != deleteCnt 이므로 동기화 진행 X)

다시 최대힙에서 pop을 시도할 시, 동기화가 안됐으므로 3이 아닌 5가 pop이 된다.
"""

# 우선순위 큐는 '완전 이진 트리' 구조이다.
# 우선순위 큐 insert/pop 과정 (minHeap 기준)
    # insert
    # 1) 리프노드에 insert 된다.
    # 2) 부모노드와 비교하여 작을 시, 교환한다. (반복)
    # delete
    # 1) 루트노드가 pop 된다.
    # 2) 리프노드를 부모노드로 올린다.
    # 3) 자식노드 중 더 작은 노드와 교환한다. (반복)


# I n : n 삽입
# D 1 : 최댓값 삭제, 하나만 삭제, 비어있는 경우 무시
# D -1 : 최솟값 삭제
import heapq
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""minPQ, maxPQ insert/pop 진행하는 함수"""
def pqFuction(maxPQ, minPQ, operator, num, numDict):
    if operator == "I":
        heapq.heappush(minPQ, num)
        heapq.heappush(maxPQ, -num)
        numDict[num] += 1

    elif operator == "D":
        if num == 1 and maxPQ: # 최댓값 삭제
            dictPop(maxPQ, numDict, -1)

        elif num == -1 and minPQ: # 최솟값 삭제
            dictPop(minPQ, numDict, 1)


"""pop 시, 이미 삭제된 값인지 판단하여 pop하는 함수"""
def dictPop(PQ, numDict, flag):
    if numDict[flag * PQ[0]] > 0:
        numDict[flag * heapq.heappop(PQ)] -= 1
    else:
        sync(PQ, numDict, flag)
        if PQ: # 동기화 진행 이후, pop 진행
            numDict[flag * heapq.heappop(PQ)] -= 1


"""이미 삭제된 값인지 확인하여, 동기화하는 함수"""
def sync(PQ, numDict, flag):
    while True:
        if PQ and numDict[flag * PQ[0]] == 0:
            heapq.heappop(PQ)
        else:
            break


T = int(input())
for _ in range(T):
    N = int(input())

    insertCnt, deleteCnt = 0, 0
    maxPQ, minPQ = [], []
    numDict = defaultdict(int)
    for i in range(N):
        operator, numStr = map(str, input().split())
        num = int(numStr)

        pqFuction(maxPQ, minPQ, operator, num, numDict)

    # 최솟값, 최댓값 출력
    sync(maxPQ, numDict, -1)
    sync(minPQ, numDict, 1)
    if maxPQ:
        print(-heapq.heappop(maxPQ), heapq.heappop(minPQ))
    else:
        print("EMPTY")
