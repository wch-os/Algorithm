T = int(input())


for _ in range(T):

    N = int(input())
    drink = 0

    for _ in range(N):
        uni, num = map(str, input().split())
        if drink < int(num):
            drink = int(num)
            result = uni

    print(result)