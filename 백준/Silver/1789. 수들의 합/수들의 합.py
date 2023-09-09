S = int(input())

N = 1
sumN = 0
while True:
    sumN += N

    # sum값이 S를 넘으면
    # 그 전에 N-1을 더하는 대신 N+a를 더했으면 수를 완성할 수 있었다는 의미
    if sumN > S:
        break

    N += 1

print(N-1)