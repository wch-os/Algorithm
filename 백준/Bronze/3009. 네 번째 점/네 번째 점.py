x = {}
y = {}
for _ in range(3):
    a, b = map(int, input().split())
    if a in x:
        x[a] += 1
    else:
        x[a] = 1

    if b in y:
        y[b] += 1
    else:
        y[b] = 1


for key in x:
    if x[key] == 1:
        resultX = key

for key in y:
    if y[key] == 1:
        resultY = key

print(resultX, resultY)