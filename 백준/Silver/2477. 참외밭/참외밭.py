# 참고 : https://itcrowd2016.tistory.com/84
# !. 6 index = 0 index로 만들어줘야 한다.

import sys
input = sys.stdin.readline

oneGrow = int(input())

lst = []
width = 0
height = 0
for i in range(6):
    l, move = map(int, input().split())
    lst.append((l, move))

    # 동서 길이
    if l == 1 or l ==2:
        before = width
        width = max(width, move)

        if before < width:
            maxIdxW = i

    # 남북 길이
    elif l == 3 or l == 4:
        before = height
        height = max(height, move)

        if before < height:
            maxIdxH = i

# 큰 사각형의 넓이
big = width * height

# 작은 사각형의 넓이
# 가장 긴 변을 중심으로, 앞 뒤를 살펴보면 된다.
subWidth = abs(lst[maxIdxW-1][1] - lst[(maxIdxW+1) % 6][1])
subHeight = abs(lst[maxIdxH-1][1] - lst[(maxIdxH+1) % 6][1])
sub = subWidth * subHeight

print(oneGrow * (big-sub))