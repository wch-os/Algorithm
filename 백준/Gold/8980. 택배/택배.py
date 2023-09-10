# 목표 번호 1 : 15점

import heapq
import sys
sys.stdin.readline

N, C = map(int, input().split()) # 마을의 수, 트럭의 용량
M = int(input()) # 박스 정보의 개수

lst = [] # 박스 정보 데이터
for _ in range(M):
    send, receive, capacity = map(int, input().split())

    # 용량 초과일 경우
    if capacity >= C:
        capacity = C

    heapq.heappush(lst, (-capacity, send, receive))


# 보내는 마을번호는 모두 1이므로, 트럭에 최대한 가득 싣기
sumC = 0
while lst:
    capacity, start, end = heapq.heappop(lst)
    capacity = -capacity
    sumC += capacity

    if sumC >= C:
        sumC = C
        break

print(sumC)