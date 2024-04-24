dish = list(input())

result = 10
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        result += 5
    else:
        result += 10

print(result)