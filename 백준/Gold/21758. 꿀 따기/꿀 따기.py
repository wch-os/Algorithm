# 풀이 시간: 40분 + 20분
# 유형: 그리디, 누적합
# 시간복잡도: O(4n)
# 공간복잡도: O(n)
# 참고 : https://velog.io/@a87380/21758%EB%B2%88-%EA%BF%80-%EB%94%B0%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 완전탐색의 시간복잡도는 O(nC3)
# 꿀벌벌, 벌꿀벌, 벌벌꿀 경우의 수를 제한하여 탐색횟수를 줄인다.
# 2번째 벌의 움직임을 추적하여 꿀을 많이 얻어낼 수 있는 최선의 경우의 수를 찾아야 한다.


N = int(input())
honey = list(map(int, input().split()))

sumHoney = [0 for _ in range(N)] # 벌 누적합
sumHoney[0] = honey[0]
for i in range(1, N):
    sumHoney[i] = sumHoney[i-1] + honey[i]

result = 0

# 벌벌꿀
aBee = sumHoney[N-1] - honey[0] # 0 위치
for i in range(1, N-1): # 1 ~ N-2까지
    # a 벌은 b 벌이 i에 위치하면서 제외해야 함
    # b 벌은 본인이 위치한 i를 제외한 꿀을 먹는다.
    a = aBee - honey[i]
    b = sumHoney[N-1] - sumHoney[i]
    result = max(result, a + b)


# 꿀벌벌
aBee = sumHoney[N-1] - honey[N-1] # N-1 위치
for i in range(N-2, 0, -1): # N-2 ~ 1까지
    a = aBee - honey[i]
    b = sumHoney[i-1]
    result = max(result, a + b)


# 벌꿀뻘
cCase = 0
init = sum(honey[1:N-1])
for i in range(1, N-1):
    cCase = max(cCase, init + honey[i])

result = max(result, cCase)
print(result)
