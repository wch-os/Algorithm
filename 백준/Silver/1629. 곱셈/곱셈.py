# 모듈러 연산으로 푸는 거 알고 있었는데.. ㅠㅠ
# 효율적으로 줄여보겠다고😭

def divide(a, b, c):
    # 더 이상 줄일 수 없을 때까지
    if b == 1:
        return a % c

    elif b % 2 == 0:
        return (divide(a, b//2, c) ** 2) % c

    else:
        return (divide(a, b//2, c) ** 2 * a) % c



A, B, C = map(int, input().split())

# A^B % C
print(divide(A, B, C))