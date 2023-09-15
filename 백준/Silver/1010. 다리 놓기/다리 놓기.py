import math

T = int(input())
for _ in range(T):
    # 서쪽과 동쪽에 있는 사이트 개수
    W, E = map(int, input().split())

    n_fact = math.factorial(E)
    r_fact = math.factorial(W)
    n_r_fact = math.factorial(E-W)

    # 동쪽에 있는 다리 E개 중, W개만큼 선택
    print(n_fact // r_fact // n_r_fact)