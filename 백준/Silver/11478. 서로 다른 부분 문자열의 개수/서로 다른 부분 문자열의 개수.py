# 재귀 깊이 설정, 이 문제에서는 최대 50만까지 갈까?

import sys
sys.setrecursionlimit(10**9)

def solve(start):
    # start ~ len(s) : 0 ~ len(s), 1 ~ len(s) ...
    # 이렇게 len(s) 가 될 때까지 탐색
    if start == len(s):
        return

    for i in range(start, len(s)):
        result.add(s[start:i+1])

    solve(start+1)


s = input() # 입력받은 문자열

result = set() # 부분 문자열 저장하는 set
solve(0)
print(len(result))