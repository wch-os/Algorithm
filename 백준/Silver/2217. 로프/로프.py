import sys
import heapq
input = sys.stdin.readline

N = int(input()) # N개의 로프

weight = []
for _ in range(N):
    weight.append(int(input()))

# 내림차순 정렬
weight.sort(reverse=True)

# 로프들을 이용해서 들어올릴 수 있는 물체의 최대 중량
maxWeight = 0

# n개 or n-1개
for i in range(N):
    maxWeight = max(maxWeight, weight[i] * (i+1))

print(maxWeight)