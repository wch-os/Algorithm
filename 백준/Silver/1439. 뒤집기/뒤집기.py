s = input()

zeroCount = 0
oneCount = 0
sequence = True
if s[0] == "0":
    zeroCount += 1
else:
    oneCount += 1

for i in range(len(s)-1):
    # 연속적이지 않으면, 그 다음 숫자 기준으로 카운트
    if s[i] != s[i+1]:
        sequence = False
        if s[i+1] == "0":
            zeroCount+=1
        else:
            oneCount+=1

# 카드를 뒤집는 행동의 최소 횟수
print(min(zeroCount, oneCount))