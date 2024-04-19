T = int(input())

for _ in range(T):
    scoreY, scoreK = 0, 0
    for _ in range(9):        
        y, k = map(int, input().split())
        scoreY += y
        scoreK += k
    
    if scoreY > scoreK:
        print("Yonsei")
    elif scoreY < scoreK:
        print("Korea")
    else:
        print("Draw")