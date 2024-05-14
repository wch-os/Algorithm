def check():
    for i in range(len(alpha)//2 + 1):
        if alpha[i] != alpha[-(i + 1)]:
            return 0

    return 1

alpha = input()
print(check())