N = int(input())

result = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    a, b, c = lst[0], lst[1], lst[2]

    if a == b == c:
        result = max(result, 10000 + a * 1000)
    elif a == b or b == c:
        result = max(result, 1000 + b * 100)
    elif c == a:
        result = max(result, 1000 + c * 100)
    else:
        result = max(result, max(lst) * 100)

print(result)