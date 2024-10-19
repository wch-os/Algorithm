# 풀이 시간: 15분
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: stack
# 참고: -

# A 탑의 레이저 신호를 수신하는 B 탑의 번호를 찾아야 한다. 이 때, 탑의 번호는 1번부터 시작한다.
# 따라서 stack에는 '레이저 신호를 수신하지 못하는 탑의 번호'를 리스트로 관리하고
# 수신 가능한 탑이 나왔을 시, pop()을 하면서 수신한 탑의 번호를 value로 지정한다.

N = int(input()) # 탑의 수
lst = list(map(int, input().split()))

stack = []
result = [0] * N


for i in range(N-1, -1, -1):
    while stack and lst[stack[-1]] < lst[i]:
        result[stack.pop()] = i + 1

    stack.append(i)

print(*result)