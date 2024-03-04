# 풀이 시간 : 7분
# 시간복잡도 : O(E-N)
# 공간복잡도 : O(E)
# 참고 : -

S = list(input())
E = list(input())

while len(S) != len(E):
    if E[-1] == 'A':
        E.pop()
    elif E[-1] == 'B':
        E.pop()
        E.reverse()

if S == E:
    print(1)
else:
    print(0)