# 풀이 시간 : 20분
# 시간복잡도 : O(N)
# 공간복잡도 : O(N)
# 참고 : -

# sum 값의 양수, 음수로 포인터를 조정
# 20번째 라인 abs(se)
# while s < len(lst) and e >= 0
    # 이전 7453 문제에서는 2개의 리스트를 투포인터로 계산을 해 중첩이 되도 상관이 없었다.
    # 이 문제는 1개의 리스트에서 투포인터 계산을 하므로 같은 인덱스를 가리키면 안된다.
    # 따라서 s 가 e 를 역전할 때 break 되어야 한다.

def twoPointer():
    s = 0
    e = len(lst) - 1

    minValue = float('inf')
    A, B = 0, 0
    while s < e:
        se = lst[s] + lst[e]

        if abs(se) < minValue:
            A, B = lst[s], lst[e]
            minValue = abs(se)

        if se < 0:
            s += 1
        else:
            e -= 1

    return A, B


N = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = twoPointer()
print(result[0], result[1])