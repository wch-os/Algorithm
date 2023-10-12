from collections import deque

# 입력
n = int(input())
lst = list(map(int, input().split()))

# deque에 저장 (풍선 안에 있는 종이, 풍선 번호)
idx = 1
ballones = deque()
for s in lst:
    ballones.append((s, idx))
    idx += 1


# 0번째 인덱스를 기준으로, 터트려야 할 풍선 배열
result = []
while True:
    # 터트려야 할 풍선
    value, idx = ballones.popleft()
    result.append(idx)

    if len(ballones) == 0:
        break

    # 양수일 경우, 오른쪽으로 이동(popleft를 value번)
    if value > 0:
        for _ in range(value-1):
            ballones.append(ballones.popleft())

    else:
        for _ in range(-value):
            ballones.appendleft(ballones.pop())

# 결과 출력
for k in result:
    print(k, end=" ")