def check():
    divisor = []
    for i in range(1, num):
        if num % i == 0:
            divisor.append(i)

    if num == sum(divisor):
        return divisor

    return False


while True:
    num = int(input())
    if num == -1:
        break

    result = check()
    if result:
        print(num, " = ", " + ".join(str(i) for i in result), sep="")
    else:
        print(f"{num} is NOT perfect.")

