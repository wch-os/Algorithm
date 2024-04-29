import sys
input = sys.stdin.readline

N = int(input())

one, two, three, four, axis = 0, 0, 0, 0, 0
for _ in range(N):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        one += 1
    elif x < 0 and y > 0:
        two += 1
    elif x < 0 and y < 0:
        three += 1
    elif x > 0 and y < 0:
        four += 1
    else:
        axis += 1

print(f"Q1: {one}")
print(f"Q2: {two}")
print(f"Q3: {three}")
print(f"Q4: {four}")
print(f"AXIS: {axis}")