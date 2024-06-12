# 풀이 시간: 30분 + 30분
# 시간복잡도: O(N * K)
    # N: 수행해야 할 작업 개수
    # K: 선행 관계에 있는 작업 개수
# 공간복잡도: O(N)
# 유형: dp
# 참고: -

# 몇 개의 일을 동시에 할 수 있는지 한계가 있는 것이 아니다.
# 따라서 할 수 있는 일들은 바로 시작하자.

# 4
# 10 0
# 6 1 1
# 7 1 1
# 5 1 2
# : 3번 작업과 5번 작업이 연결되어 있다.

import sys
input = sys.stdin.readline

def solve():
    # dp[i]: i작업을 수행하는데 걸리는 최소 시간
    dp = [0] * N
    dp[0] = lst[0][0]

    for i in range(1, N):
        currWorksTime = lst[i][0] # i작업을 하는데 걸리는 시간
        prevWorks = lst[i][2:]  # i작업을 수행하기 전, 선행 관계에 있는 작업들 번호

        # 선행 작업이 없을 경우, 현재 작업 걸리는 시간 그대로 저장
        if len(prevWorks) == 0:
            dp[i] = currWorksTime
            # 선행 작업이 있을 경우
        else:
            for prevWork in prevWorks:  # j: 선행 관계에 있는 작업들의 번호
                dp[i] = max(dp[i], dp[prevWork - 1] + currWorksTime)  # 1번 작업은 0번 작업을 의미한다.

    return max(dp)



N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

print(solve())