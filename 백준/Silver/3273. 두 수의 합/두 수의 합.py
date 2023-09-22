# 투포인터 첫 문제

n = int(input()) # 수열의 크기
lst = list(map(int, input().split()))
x = int(input())

lst.sort()

sp, ep = 0, n-1
count = 0

while sp < ep:
    if lst[sp] + lst[ep] == x:
        count += 1
        ep -= 1 # sp를 바꿔도 됨

    elif lst[sp] + lst[ep] > x:
        ep -= 1

    elif lst[sp] + lst[ep] < x:
        sp += 1

print(count)