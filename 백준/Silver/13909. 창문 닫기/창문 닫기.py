# 약수의 개수가 짝수이면 닫힘 / 홀수이면 열림
# 소수이면 약수가 무조건 2개
# 어떤 수 X를 소인수분해하면 a * b → (a의 지수+1) * (b의 지수+1) = 약수의 개수 | 여기에서 a,b는 소인수
# 약수의 개수가 짝수이려면 a의 지수가 짝수이고, b의 지수는 0, 즉 없어야한다.
# 이 수는 제곱수밖에 없다.

N = int(input())

i = 1
while True:
    i += 1

    # 제곱수가 N 범위를 벗어나면 break
    if i * i > N:
        break

print(i-1)