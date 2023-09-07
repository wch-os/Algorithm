import sys
import heapq
input = sys.stdin.readline

N = int(input()) # N개의 로프

weight = []
for _ in range(N):
    heapq.heappush(weight, int(input()))

# 로프들을 이용해서 들어올릴 수 있는 물체의 최대 중량
maxWeight = 0

# 우선순위 큐가 비어있지 않으면
# 해당 로프를 사용하지 않는 것이 이득인지, 사용하는 것이 이득인지 판단
while weight:
    maxWeight = max(maxWeight,heapq.heappop(weight)*N)
    N-=1

print(maxWeight)