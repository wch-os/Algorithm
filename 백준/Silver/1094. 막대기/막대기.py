x = int(input())

# x에 포함된 '비트 1'의 개수
result = 0

# 막대의 길이는 64 = 2^6
for i in range(7):
    # 'x'와 비트 AND 연산을 통해, 'i'번째 비트가 1로 설정되어 있는지 확인
    if x & (1<<i):
        result += 1

print(result)