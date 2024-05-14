H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    if H == 0: # 0시
        H = 23
    else:
        H -= 1
    M = 60 - (45 - M)

print(H, M)