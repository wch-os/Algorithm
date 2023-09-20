# 이전 코드는 combination(누적합, 2)로 시간복잡도가 O(nC2)이다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ary = list(map(int, input().split()))

# SUM[i] : i인덱스까지의 누적합 (1인덱스 기준)
SUM = [0] * (len(ary) + 1)

# MOD[i] : 누적합을 %M 했을 때, 나머지가 i인 수
MOD = [0] * M
for i in range(1, len(ary)+1):
    SUM[i] = SUM[i-1] + ary[i-1]
    MOD[SUM[i]%M] += 1

# (SUM[i] - SUM[j]) % M == 0 일 때, 나머지가 1 ~ M-1인 부분누적합 개수 찾기
# 문제의 답은, 만족하는 (i,j)의 개수를 찾으면 된다.
# 모듈러 연산에 의해
# "SUM[i] % M = SUM[j] % M" 을 만족하는 (i,j)를 찾으면 된다.  → nC2
result = MOD[0]
for i in range(0, M):
    result += (MOD[i] * (MOD[i]-1)) // 2

print(result)