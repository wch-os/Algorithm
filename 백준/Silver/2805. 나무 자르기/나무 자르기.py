def solve(start, end):
    # 역전 구간에 exit()
    if start > end:
        print(end)
        exit()

    mid = (start + end) // 2

    have = 0
    for item in lst:
        if item >= mid:
            have += (item - mid)

    # 더 많이 챙겼다면, 더 높은 곳에서 자르자
    if have >= M:
        solve(mid+1, end)

    elif have < M:
        solve(start, mid-1)

# 나무의 수, 가지고 가려고 하는 나무의 길이
N, M = map(int, input().split())
lst = list(map(int, input().split()))

solve(0, max(lst))