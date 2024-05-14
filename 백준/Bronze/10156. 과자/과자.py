price, num, money = map(int, input().split())

result = price * num - money
if result > 0:
    print(result)
else:
    print(0)