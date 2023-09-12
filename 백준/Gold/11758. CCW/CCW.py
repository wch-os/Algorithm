# 벡터의 외적으로, 방향성 판단
# 참고 : https://degurii.tistory.com/47

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def CCW():
    a = (x2-x1) * (y3-y1)
    b = (x3-x1) * (y2-y1)
    return a - b

result = CCW()

# 일직선
if result == 0:
    print(0)

# 반시계 방향
elif result > 0:
    print(1)

# 시계 방향
elif result <0:
    print(-1)