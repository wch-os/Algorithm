# 참고 : https://velog.io/@kimdukbae/BOJ-14725-%EA%B0%9C%EB%AF%B8%EA%B5%B4-Python

import sys
input = sys.stdin.readline

N = int(input().strip())

cave = []
depth = 0
for _ in range(N):
    lst = list(map(str, input().strip().split()))
    depth = max(depth, int(lst[0]))
    cave.append(lst[1:]) # cave 정렬을 위해서 삭제해야 함

cave.sort()

result = [] # 결과
top = [] # 루트 자식노드 리스트

for i in range(N):
    if i == 0:
        for j in range(len(cave[i])):
            result.append(("--" * j) + cave[i][j])

    else:
        idx = 0
        for j in range(len(cave[i])):
            # 이전 정보와 겹치지 않거나, 겹치다가 현재 동굴의 길이가 더 깊을 때
            if cave[i-1][j] != cave[i][j] or len(cave[i-1]) <= j: # j → len(cave[i])
                break
            else:
                idx = j + 1

        for j in range(idx, len(cave[i])):
            result.append("--" * j + cave[i][j])

for r in result:
    print(r)