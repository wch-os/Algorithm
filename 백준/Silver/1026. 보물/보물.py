N = int(input())

lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))

sortA = sorted(lstA) # 오름차순
sortB = sorted(lstB, reverse=True) # 내림차순

minSum = 0
for i in range(N):
    minSum += sortA[i] * sortB[i]

print(minSum)