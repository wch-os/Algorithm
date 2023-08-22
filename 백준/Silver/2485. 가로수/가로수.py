import sys
from math import gcd
input = sys.stdin.readline

#심어져 있는 가로수 개수
N = int(input())

#가로수 위치 입력
location = []
for _ in range(N):
    location.append(int(input()))

#가로수 사이 간격 찾기
gaps = []
for i in range(N-1):
    gaps.append(location[i+1]-location[i])

#간격, 최대공약수 찾기
gapGcd = gaps[0]
for i in range(1, N-1):
    gapGcd = gcd(gapGcd, gaps[i])

#같은 간격이 되도록 심어야 하는 가로수의 최소 개수
    #간격을 최대공약수로 나누면, 간격 사이에 존재해야 하는 나무 개수를 알 수 있다.
    #이미 그 사이에 나무가 1개가 심어져 있으므로 -1
result = 0
for i in gaps:
    result = result + i // gapGcd - 1

print(result)
