# 풀이 시간 : 10 + 25분
# 시간복잡도 : O(N)
# 공간복잡도 : O(1)
# 참고 : -

# 1 2 6 24 120 720(6!) 5040(7!)
# 0이 아닌 숫자가 나올 때까지의 수에서 팩토리얼을 계속 계산하자

# 첫번째 제출 코드
    # 1의 자리만 남는 코드가 아니다.
    # 결국 fact가 INF 값이 되고 만다.

    # 1의 자리만 남게 하면 된다.

N = int(input())

fact = 1
zeroCount = 0
for i in range(1, N + 1):
    fact *= i

    # 10으로 나눠질 경우
    if fact % 10 == 0:
        while True:  # 1의 자리만 남기도록 한다.
            if fact % 10 != 0:
                fact %= 10
                break

            fact /= 10
            zeroCount += 1

print(zeroCount)