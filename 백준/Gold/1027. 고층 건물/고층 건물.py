def solve():
    result = 0
    for i in range(N):
        cnt = 0

        leftSlope = float('inf')
        rightSlope = -float('inf')
        for j in range(i-1, -1, -1): # 왼쪽: 기울기가 작아져야 한다.
            x = i - j
            y = buildings[i] - buildings[j]

            slope = y / x
            if leftSlope > slope:
                leftSlope = slope
                cnt += 1


        for j in range(i+1, N): # 오른쪽: 기울기가 커져야 한다.
            x = i - j
            y = buildings[i] - buildings[j]

            slope = y / x
            if rightSlope < slope:
                rightSlope = slope
                cnt += 1

        result = max(result, cnt)

    return result


N = int(input())
buildings = list(map(int, input().split()))

print(solve())