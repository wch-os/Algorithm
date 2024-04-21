N = int(input())
scoreA, scoreB = 100, 100
for _ in range(N):
    a, b = map(int, input().split())

    if a > b:
        scoreB -= a
    elif a < b:
        scoreA -= b

print(scoreA)
print(scoreB)