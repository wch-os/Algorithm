import math
import sys
input = sys.stdin.readline

end = 1000000 # 문제의 범위
prime = [True] * (end+1) # True : 소수

def part(n):
    count = 0
    for i in range(2, n//2+1): # 순서만 다른 것은 같은 파티션
        if prime[i] and prime[n-i]:
            count += 1

    return count

T = int(input())

# 에라토스테네서의 채로 소수 판별하기
for i in range(2, int(math.sqrt(end+1))):
    for j in range(i*i, end, i):
        prime[j] = False
prime[0] = False
prime[1] = False

for _ in range(T):
    N = int(input())
    print(part(N))