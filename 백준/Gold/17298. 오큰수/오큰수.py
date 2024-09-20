N = int(input())
lst = list(map(int, input().split()))
NGE = [-1] * N

idx = -1
indexStack = []
for num in lst:

    idx += 1
    while indexStack and lst[indexStack[-1]] < num:
        NGE[indexStack.pop()] = num

    indexStack.append(idx)

print(*NGE)