A = int(input())
T = int(input())
what = int(input())

result = []

n = 0
degiCnt = 0
while True:
    n += 1 # n회차
    lst = [0, 1, 0, 1]
    lst += (n + 1) * [0] + (n + 1) * [1]
    result += lst
    
    degiCnt += 2 + n + 1 # 회차 시, 뻔 or 데기 갯수
    
    if degiCnt > T:
        x = degiCnt - T + 1 # 뒤에서 x번째 what 인덱스 % A를 하면 된다.

        whatCount = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] == what:
                whatCount += 1
                if whatCount == x:
                    print(i % A)
                    exit()