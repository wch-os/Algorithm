""" 동일한 키가 있을 경우의 알고리즘 """

import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

stack = []
result = 0

# num을 기준으로 이전 원소 중 조건에 부합하 원소들만을 stack에서 관리하여, 만족하는 쌍을 찾도록 한다.
for num in lst:

    # stack에 num을 기준으로 높은 수만 있다. (내림차순)
    while stack and stack[-1][0] < num:
        result += stack.pop()[1]


    if stack:
        if stack[-1][0] == num:
            cnt = stack.pop()[1]
            result += cnt

            # 동일한 원소를 pop() 했음에도, 여전히 stack에 원소가 남아있으면 이는 num보다 큰 수로 바라볼 수 있는 수이다.
            if stack:
                result += 1

            stack.append((num, cnt + 1))


        # stack은 내림차순으로 정렬되어 있으므로, num에서 볼 수 있는 원소는 stack[-1] 밖에 없다.
        elif stack[-1][0] > num:
            result += 1
            stack.append((num, 1))

    # stack이 비어 있는 경우
    else:
        stack.append((num, 1))

print(result)