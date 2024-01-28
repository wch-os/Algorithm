# 풀이 시간 : 40분 + 30분
# 시간복잡도 : O(N^2)
# 공간복잡도 : O(N)
# 참고 : https://kdr0407.tistory.com/33

# 완전탐색
    # N * (N-1) * (N-2) / 3! = 200억
# 이분탐색
    # 2개를 임의로 선정하여 sum, sum과 가까운 k 값 찾기
    # N * (N-1) * logN = 3억

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

# 모두 양수인 경우
if lst[0] > 0:
    print(lst[0], lst[1], lst[2])

# 모두 음수인 경우
elif lst[-1] < 0:
    print(lst[-3], lst[-2], lst[-1])

else:
    minSum = float('inf')
    ans = []

    # i 고정, i+1 시작점, N-1 끝점
    for i in range(len(lst)):
        s = i+1
        e = N-1

        # 투포인터
        while s < e:
            val = lst[i] + lst[s] + lst[e]
            if minSum > abs(val):
                minSum = abs(val)
                ans = [lst[i], lst[s], lst[e]]

            # 이분탐색과 비슷
            # 총합이 음수인 경우, s++
            if val < 0:
                s += 1
            # 총합이 양수인 경우, e--
            else:
                e -= 1

    print(*ans)