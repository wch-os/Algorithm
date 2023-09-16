import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hearName = set()
for _ in range(N):
    hearName.add(input().rstrip())

result = []
for _ in range(M):
    s = input().rstrip()

    if s in hearName: #교집합이면
        result.append(s)


# 사전순으로 정렬
result.sort()

print(len(result))
for item in result:
    print(item)
