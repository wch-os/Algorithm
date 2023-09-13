# 벡터의 외적으로, 방향성 판단
# 참고 : https://degurii.tistory.com/47

x1, y1 = map(int, input().split()) # 점 A
x2, y2 = map(int, input().split()) # 점 B
x3, y3 = map(int, input().split()) # 점 C

def CCW():
    # 벡터 AB, 벡터 AC 외적한 결과 (신발끈 공식)
    a = (x2-x1) * (y3-y1)
    b = (x3-x1) * (y2-y1)

    # 벡터 AB X 벡터 AC = 평행사변형 넓이, 그리고 방향을 알 수 있음
    return a - b

result = CCW()

# 일직선
if result == 0:
    print(0)

# 반시계 방향
elif result > 0:
    print(1)

# 시계 방향
elif result < 0:
    print(-1)