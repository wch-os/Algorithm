N, D = map(int, input().split())

minList = [10001] * (D + 1)  #각 지점까지 오는데 걸리는 최소 비용 MAX로 초기화
nodes = [[] for _ in range(10001)] #지름길 정보 입력받기, [] : 도착 / [i].add(시작, 비용)

for i in range(N):
    start, end, cost = map(int, input().split())
    nodes[end].append((start, cost))

minList[0] = 0 #0까지의 최소 거리는 0
for i in range(1, D + 1):
    if not nodes[i]: #목적지까지의 지름길 정보가 존재하지 않는 경우 
        minList[i] = minList[i - 1] + 1

    else: #목적지까지의 지름길 정보가 존재할 경우
        for j in range(len(nodes[i])):
            minD = min(minList[i - 1] + 1, minList[nodes[i][j][0]] + nodes[i][j][1]) #직전 길에서 +1 한 값과, 0~출발지점까지의 비용 + 지름길 비용한 값을 비교
            minList[i] = min(minList[i], minD) #지름길이 여러 개 있을 경우를 위한 비교

print(minList[D])
