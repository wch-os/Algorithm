n = int(input())
lst = list(map(int, input().split()))

minNum = min(lst)

for i in range(1, minNum+1):
    count = 0
    for l in lst:
        if l % i != 0:
            break

        count += 1
        if count == len(lst):
            print(i)