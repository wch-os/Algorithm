# 참고 : https://ddiyeon.tistory.com/36
# 참고 : https://hillier.tistory.com/105

import sys
sys.stdin.readline

N, C = map(int, input().split()) # 마을의 수, 트럭의 용량
M = int(input()) # 박스 정보의 개수
infos = []

lst = [] # 박스 정보 데이터
for _ in range(M):
    send, receive, box = map(int, input().split())
    infos.append((send, receive, box))

# 빠른 도착지를 기준으로 오름차순 정렬한다.
infos.sort(key = lambda x : x[1])

# 각 마을에서 실을 수 있는 트럭 용량
vilCapa = [C] * N
total = 0

for s, r, box in infos:
    _min = C

    # 각 마을에서 실을 수 있는 용량 계산하기
    for i in range(s, r):
        # 해당 범위에서 보낼 수 있는 박스 중, 최소에 맞춘다.
        if _min > min(vilCapa[i], box):
            _min = min(vilCapa[i], box)

    # 트럭에 실은만큼, 실을 수 있는 용량을 재계산한다.
    for i in range(s, r):
        vilCapa[i] -= _min

    # 실었던 박스를 더한다.
    total += _min

print(total)