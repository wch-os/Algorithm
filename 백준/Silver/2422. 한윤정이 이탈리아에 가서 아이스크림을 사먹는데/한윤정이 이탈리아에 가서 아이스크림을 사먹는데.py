# 풀이 시간 : 20분 + 10분
# 시간복잡도 : O(nC3)
# 공간복잡도 : O(N or M)
# 참고 : https://changsroad.tistory.com/133

import itertools
import sys
input = sys.stdin.readline

# N : 아이스크림 종류의 수, M : 섞어먹으면 안 되는 조합의 개수
N, M = map(int, input().split())

# 금지된 조합
exhibit = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    exhibit[a-1][b-1] = True
    exhibit[b-1][a-1] = True

count = 0
for i in itertools.combinations(range(N), 3):
    # i : 3가지 아이스크림 맛
    # 3쌍 중에 1가지라도 금지된 조합이 있을 시
        # 해당 맛 조합은 채용해서는 안된다.
    if exhibit[i[0]][i[1]] or exhibit[i[1]][i[2]] or exhibit[i[2]][i[0]]:
        continue

    count += 1

print(count)