N = int(input()) # 센서의 개수
K = int(input()) # 집중국의 개수
location = list(map(int, input().split())) # 각 센서의 위치

# 집중국의 수가 센서보다 같거나 많다면
if K >= N:
    print(0)

else:
    # 센서, 오름차순 정렬
    location.sort()

    # 센서들간의 거리, 내림차순 정렬
    gap = []
    for i in range(len(location)-1):
        gap.append(location[i+1] - location[i])
    gap.sort(reverse=True)

    # 거리가 긴 센서들부터 minus
    result = sum(gap)
    for i in range(K-1):
        result -= gap[i]

    print(result)