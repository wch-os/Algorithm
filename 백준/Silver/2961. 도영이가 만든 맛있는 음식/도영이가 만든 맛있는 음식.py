# BruteForce

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

# 부분집합 만들기, O(2**N)
subsets = []
for i in range(1, 2**N):
    subsetA = []
    subsetB = []
    for j in range(N):
        if (i >> j) % 2 == 1: # 음...
            subsetA.append(lst[j][0])
            subsetB.append(lst[j][1])

    subsets.append((subsetA, subsetB))


# (* +)의 최소값 출력
_min = float('INF')
for subsetA, subsetB in subsets:
    mulA = 1
    for item in subsetA:
        mulA *= item

    sumB = sum(subsetB)

    _min = min(_min, abs(mulA-sumB))

print(_min)