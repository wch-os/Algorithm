# BruteForce
import itertools

N = int(input())

sour = []
bit = []
for _ in range(N):
    a, b = map(int, input().split())
    sour.append(a)
    bit.append(b)

# 1~N 까지의 조합
sourCom = []
bitCom = []
for i in range(1, N+1):
    #extend : list 안에 list가 아니라 병합되게 처리
    #itertools.combinations : 리스트 내의 원소로 조합
    sourCom.extend(list(itertools.combinations(sour, i)))
    bitCom.extend(list(itertools.combinations(bit, i)))


# (* +)의 최소값 출력
_min = float('INF')
for sour, bit in zip(sourCom, bitCom): # zip() 사용
    mulA = 1
    for i in sour:
        mulA *= i
    sumB = sum(bit)
    
    _min = min(_min, abs(mulA-sumB))

print(_min)