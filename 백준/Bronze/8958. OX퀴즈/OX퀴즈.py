N = int(input())
for _ in range(N):
    quiz = input()
    
    cnt = 0
    sumCnt = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            cnt += 1
        else:
            cnt = 0
        sumCnt += cnt
    
    print(sumCnt)