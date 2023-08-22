import math
import sys
input = sys.stdin.readline

def solve(N):
    #0과 1은 소수가 아니다.
    if N==0 or N==1:
        return False

    #소수 판별
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False

    return True


T = int(input())
for i in range(T):
    N = int(input())

    while True:
        prime = solve(N)

        #소수일 경우, 출력하고 break
        if prime:
            print(N)
            break

        #소수가 아닐 경우, N보다 큰 소수를 찾기 위해 +1
        else:
            N += 1