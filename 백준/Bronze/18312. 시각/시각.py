N, K = map(int, input().split())

hour, minute, second = 0, 0, 0

cnt = 0
result = []
while True:
    if second == 60:
        minute += 1
        second = 0

    if minute == 60:
        hour += 1
        minute = 0

    if hour == N+1:
        break

    if second % 10 == K or second // 10 == K or minute % 10 == K or minute // 10 == K or hour % 10 == K or hour // 10 == K:
        cnt += 1
        result.append((hour, minute, second))

    second += 1

print(cnt)