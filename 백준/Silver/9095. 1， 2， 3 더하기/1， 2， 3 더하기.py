#사용하는 자료구조
dp = [0] * 12

#테스트 케이스 갯수
T = int(input())

#DP 알고리즘
def solve(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4

    else:
        return solve(N-1) + solve(N-2) + solve(N-3)

#입력
for i in range(T):
    N = int(input())
    print(solve(N))