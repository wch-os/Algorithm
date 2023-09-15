# EOF 입력받는 문제에서는 sys.stdin.readline을 사용하면 안된다..?

def divide(n):
    # 1이 될 때까지 잘게 쪼갠다.
    if n == 1:
        return '-'

    scope = n // 3

    # 0 ~ scope
    left = divide(scope)
    # 중간 구간은 공백 그대로 출력
    center = ' ' * scope

    return left + center + left


while True:
    try:
        s = input()

        # 빈 문자열인 경우, break
        if s == "":
            break

        # 초기 칸토어 집합
        _input = pow(3, int(s))


        result = divide(_input)
        print(result)

    except EOFError:
        break