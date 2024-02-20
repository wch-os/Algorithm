a, b = map(int, input().split())

# 의자 각도 저장
circle = set()

for i in range(a, b+1):
    init = 360 / i
    k = init

    if init not in circle:
        while init <= 360:
            circle.add(init)
            init += k

print(len(circle))