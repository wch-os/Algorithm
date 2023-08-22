from math import gcd
def gcd_of_list(lst):
    a = lst[0]
    for b in lst[1:]:
        a = gcd(a, b)
    return a


N = int(input())

#가로수 위치 입력
location = []
for _ in range(N):
    location.append(int(input()))

#간격들 최대공약수 찾기
gaps = []
for i in range(len(location) - 1):
    gap = location[i+1] - location[i]
    gaps.append(gap)

minGap = gcd_of_list(gaps)

#심어야 할 가로수 세기
s = location[0]
e = location[len(location)-1]

print(int((e - s) / minGap) - len(location) + 1)