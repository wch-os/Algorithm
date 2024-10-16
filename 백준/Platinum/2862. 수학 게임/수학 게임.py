# 풀이 시간: -
# 시간복잡도: O(1)
# 공간복잡도: O(1)
# 유형: math
# 참고: https://steady-coding.tistory.com/222

# 경우의 수가 많아져, N개에 대한 result 케이스를 찾는 것 또한 힘든 문제인 것 같다.
# 수학적 규칙을 찾기 위해서는 적어도 13에서 21까지 result 값을 정확히 추론해야 한다.

"""
동전이 N개가 있을 때, 첫 번째 턴에서 동전을 몇 개(result) 가져가야 이길 수 있는가?

1. N에 따른 result가 어떻게 되는지 구한다.
2. 규칙을 찾는다.
3. N이 피보나치 수일 때는, result=N 이어야 한다.
4. 피보나치 수 사이의 N 값들에 대한 result 값이 어떤 규칙을 갖는지 찾는다.
5. 피보나치 수가 아닌 수의 N들은, N보다 작은 가장 큰 피보나치 수를 뺀 값을 result로 갖는다.
"""


# 피보나치 수
# 1 2 3 5 8 13 21 34

fibo = [0, 1]
for i in range(2, 100):
    fibo.append(fibo[i-1] + fibo[i-2])

N = int(input())
while True:
    # 1. N 이하의 가장 큰 피보나치 수를 구한다.
    temp = N
    for i in range(2, 100):
        if temp < fibo[i]:
            temp = fibo[i-1]
            break


    # 2. N 자체가 피보나치 수일 경우, 무조건 N으로 시작해야 한다.
    if temp == N:
        break

    N -= temp

print(N)