T = int(input())
for _ in range(T):
    a, b = map(str, input().split())

    a = int(a)
    
    result = ""
    for k in b:
        result += a*k
        
    print(result)