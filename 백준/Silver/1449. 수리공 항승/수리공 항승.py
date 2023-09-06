# 물이 새는 곳의 개수, 테이프의 길이
N, L = map(int, input().split())

hole = list(map(int, input().split()))
sortHole = sorted(hole) # 순서대로 테이프를 붙이기 위해, 오름차순 정렬

tapeLocation = 0 # 현재 붙여져 있는 테이프 위치
count = 0 # 필요한 테이프 개수 카운트

for i in sortHole:
    if tapeLocation < i+0.5:
        tapeLocation = (i-0.5) + L # 테이프 사용
        count += 1

print(count)