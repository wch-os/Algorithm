x = int(input())

own = [64]
count = 0

while True:
    # 1. 합이 x보다 크다.
    if sum(own) > x:
        # 1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
        divide = own.pop() // 2
        own.append(divide)
        own.append(divide)

        # 가정(절반 중 하나를 버리고, 남아있는 막대의 길이의 합이 X보다 크거나 같으면)
        ifpop = own.pop()
        if sum(own) >= x:
            # 그대로 버린다.
            continue
        # 가정이 빗나갔으니, 다시 append 한다.
        else:
            own.append(ifpop)

    # 막대를 풀로 붙이는 행위
    count += 1
    if sum(own) == x:
        break
        
print(count)