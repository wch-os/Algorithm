# 풀이 시간: 15분(문제이해;;) + 45분(풀이) + 15분(시간초과) + a
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: stack
# 참고: https://0902.tistory.com/57

# 1~2번째 풀이
# - A > B 로 끝날 때, cnt를 적절히 처리하지 못한다.
# - 반례: 4 5 5 5 6


import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

stack = []
result = 0 # 서로 볼 수 있는 쌍의 수
cnt = 0 # 자신을 포함하여 현재 스택에 같은 값을 가진 사람의 수

for now in lst:

    # A(now) > B(top)
    while stack and now > stack[-1][0]:
        result += stack.pop()[1]

    # 스택이 비어있을 때
    if not stack:
        stack.append((now, 1))
        continue


    # A(now) = B(top)
    if stack[-1][0] == now:

        cnt = stack.pop()[1]
        result += cnt

        # B(top)보다 큰 수가 아직 남아있다. ex. 10 1 1 1 5
        if stack:
            result += 1

        stack.append((now, cnt + 1))

    # A(now) < B(top)
    else:
        result += 1
        stack.append((now, 1))


print(result)