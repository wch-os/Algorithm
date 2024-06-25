# 풀이 시간: 35분 + 17분
# 시간복잡도: O(N)
# 공간복잡도: O(3)
# 유형: dp
# 참고: https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2096%EB%B2%88-%EB%82%B4%EB%A0%A4%EA%B0%80%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 빠른 입력 추가
# 메모리를 사용을 최소화하기 위한 풀이이다.

import sys
input = sys.stdin.readline

N = int(input())
board = list(map(int, input().split()))

# 매 row마다 dpMin, dpMax가 바뀌므로 깊은 복사를 할 필요가 없다.
dpMin = board
dpMax = board

# O(N)
for i in range(1, N):
    row = list(map(int, input().split()))

    # row가 값에 따라 이전 좌우 값을 불러오고, 저장하면 된다.
    dpMin = [row[0] + min(dpMin[0], dpMin[1]), row[1] + min(dpMin[0], dpMin[1], dpMin[2]), row[2] + min(dpMin[1], dpMin[2])]
    dpMax = [row[0] + max(dpMax[0], dpMax[1]), row[1] + max(dpMax[0], dpMax[1], dpMax[2]), row[2] + max(dpMax[1], dpMax[2])]

print(max(dpMax), min(dpMin))