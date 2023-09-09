import heapq
import sys
input = sys.stdin.readline

# 보석의 개수, 가방의 개수
N, K = map(int, input().split())

# 보석의 무게, 보석의 가격
jewel = []
for _ in range(N):
    weight, value = map(int, input().split())
    jewel.append((weight, value))

# 보석의 무게를 기준으로 오름차순 정렬, 같을 경우 가격을 기준으로 내림차순 정렬
jewel.sort(key=lambda x: (x[0], -x[1]))

bag = []
for _ in range(K):
    bag.append(int(input()))

# 무게를 기준으로 오름차순 정렬
bag.sort()


result = 0 # 훔칠 수 있는 보석 가격의 최댓값
useBag = 0 # 사용한 가방 갯수

putJewel = [] # 가방에 넣을 보석
for i in range(len(bag)):
    # 가져갈 보석이 존재하고, 보석의 무게가 | 현재 인덱스의 가방 무게보다 작을 시
    while jewel and jewel[0][0] <= bag[i]:
            w, v = heapq.heappop(jewel)
            heapq.heappush(putJewel, -v) # 가치가 높은 보석으로 내림차순 정렬을 위해, -v

    # 가방에 넣을 보석이 있다면, 그 중 제일 가치가 높은 보석을 put
    if putJewel:
        maxJewelValue = heapq.heappop(putJewel)
        result -= maxJewelValue

print(result)