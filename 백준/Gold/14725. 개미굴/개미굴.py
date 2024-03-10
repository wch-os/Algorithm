# 시간 복잡도 : O(Nlog(N) + N * K)
    # Nlog(N) : 정렬 시간 복잡도
    # N*K : 현재 동굴 정보와 이전 동굴 정보가 일치하는지 체크(K)하면서 N개의 동굴 탐색
# 공간 복잡도 : O(N)

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
    # 초기 동굴 구성
    if i == 0:
        for j in range(len(cave[i])):
            result.append(("--" * j) + cave[i][j])

    else:
        idx = 0
        for j in range(len(cave[i])):
            # 이전 정보와 겹치지 않거나, 겹치다가 현재 동굴의 길이가 더 깊어 표현할 수가 없을 때
            if cave[i-1][j] != cave[i][j] or len(cave[i-1]) <= j: # j → len(cave[i]) X
                break
            else:
                idx = j + 1

        # 겹치지 않는 시점부터, "-- + 하위 노드"를 추가한다.
        for j in range(idx, len(cave[i])):
            result.append("--" * j + cave[i][j])

for r in result:
    print(r)
