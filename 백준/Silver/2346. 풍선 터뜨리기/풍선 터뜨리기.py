from collections import deque

# 입력
n = int(input())

# deque에 저장 (풍선 번호, 풍선 안에 있는 종이)
ballones = deque(enumerate(map(int,input().split())))


# 0번째 인덱스를 기준으로, 터트려야 할 풍선 배열
result = []
while ballones:
    # 터트려야 할 풍선
    idx, value = ballones.popleft()
    result.append(idx+1)

    # 양수일 경우, rotate 기준으로 왼쪽(시계 반대방향)으로 이동
    if value > 0:
        ballones.rotate(-(value-1))

    # 음수일 경우, 왼쪽으로 이동
    else:
        ballones.rotate(-value)

# 결과 출력
for k in result:
    print(k, end=" ")