# 풀이 시간 : 20분
# 시간복잡도 : O(NlogN)
# 공간복잡도 : O(N)
# 참고 : python round() 관련 자료
#       https://blockdmask.tistory.com/418

import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

EPS = 1e-9
lst.sort()
exclude = round(N * 0.15 + EPS)

sumI = 0
for i in range(exclude, N-exclude):
    sumI += lst[i]

if sumI == 0:
    print(0)
else:
    print(round(sumI / (N-2*exclude) + EPS))