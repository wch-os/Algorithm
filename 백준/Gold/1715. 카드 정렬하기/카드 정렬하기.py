import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = list(int(input()) for _ in range(N))

#오름차순 정렬
cards.sort()
result = 0

while True:
    if len(cards) == 1:
        break

    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    c = a+b

    result += c
    heapq.heappush(cards, c)


print(result)