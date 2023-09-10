N = int(input()) # 도시의 개수

dis = list(map(int, input().split()))
price = list(map(int, input().split()))
price = price[0:len(price)-1] # 마지막 도시에서, 기름을 살 경우는 없음

location = 0 # 현재 위치
money = 0 # 목적지까지 가는데 걸리는 비용

while True:
    endArrive = True

    # 마지막 도시에 도착할 경우
    if location == N-1:
        break

    for i in range(location, len(price)):
        # 현재 지점보다, 저렴한 도시가 있다면
        if price[location] > price[i]:
            # 저렴한 도시까지 이동
            for j in dis[location:i]:
                money += (j * price[location])

            # 현재 위치 갱신, 끝까지 가는 것이 아님
            location = i
            endArrive = False
            break

    # 현재 지점보다, 저렴한 도시가 없다면
    if endArrive:
        # 현재 지점에서 목적지까지 기름 모두 구입하기
        for j in dis[location:]:
            money += (j * price[location])

        # 목적지까지 이동
        location += len(dis[location:])

print(money)