# 풀이 시간 : 28분
# 시간복잡도 : O(N * M)
# 공간복잡도 : O(N)
# 참고 : -

# 스택을 사용하는 것이 관건
# 이전 코드의 시간복잡도는 O(N*M*폭발횟수)였다.

sentence = list(input())
bomb = list(input())

N = len(sentence)
M = len(bomb)

stack = []
for i in range(N):
    stack.append(sentence[i])

    if stack[-M:] == bomb:
        for _ in range(M):
            stack.pop()

if len(stack):
    print(*stack, sep="")
else:
    print("FRULA")
