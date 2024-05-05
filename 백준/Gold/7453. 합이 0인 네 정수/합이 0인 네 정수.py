# 참고: https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-7453%EB%B2%88-%ED%95%A9%EC%9D%B4-0%EC%9D%B8-%EB%84%A4-%EC%A0%95%EC%88%98-X-1

n = int(input())

result = 0
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = dict()
for a in A:
    for b in B:
        v = a + b
        if v not in ab.keys():
            ab[v] = 1
        else:
            ab[v] += 1


for c in C:
    for d in D:
        v = -1 * (c + d)
        if v in ab.keys():
            result += ab[v]

print(result)