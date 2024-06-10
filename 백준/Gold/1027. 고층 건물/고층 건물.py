# 풀이 시간: 1시간
# 시간복잡도: O(N^2)
# 공간복잡도: O(N)
# 유형: geometry
# 참고:

# 첫번째 테스트 케이스를 이해하는데 시간이 오래 걸렸다.
# 직전 값을 이용한 기울기 증감 여부로도 접근할 수 있을 듯 

def search(idx):
    
    cnt = 0
    if 0 < idx: # idx = 0일 때 왼쪽 탐색 X
        cnt += 1 # idx 왼쪽 건물
        leftSlope = buildings[idx] - buildings[idx - 1]
        for k in range(idx - 1, -1, -1): # 왼쪽
            x = idx - k
            y = buildings[idx] - buildings[k]
            currSlope = y / x

            if leftSlope > currSlope: # 현재 기울기가 작아져야 한다.
                leftSlope = currSlope
                cnt += 1

    if idx < N - 1: # idx = N-1일 때 오른쪽 탐색 X
        cnt += 1 # idx 오른쪽 건물
        rightSlope = -(buildings[idx] - buildings[idx + 1])
        for k in range(idx + 1, N):
            x = idx - k
            y = buildings[idx] - buildings[k]
            currSlope = y / x

            if rightSlope < currSlope: # 현재 기울기가 커져야 한다.
                rightSlope = currSlope
                cnt += 1

    return cnt



N = int(input())
buildings = list(map(int, input().split()))

result = 0
for i in range(N):
    result = max(result, search(i))

print(result)