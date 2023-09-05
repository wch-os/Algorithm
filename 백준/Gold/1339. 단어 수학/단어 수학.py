N = int(input()) # N개의 단어

dic = {}
for _ in range(N):
    s = input() # 입력받는 문자열

    for i in range(len(s)): # 문자열의 각 문자
        dic[s[i]] = dic.get(s[i], 0) + pow(10, len(s)-i-1) # 각 문자의 가중치를 설정함

# 문자의 가중치를 기준으로, 내림차순 정렬 (9부터 부여하기 위함)
sortDict = dict(sorted(dic.items(), key=lambda item:item[1], reverse=True))


result = 0 # 주어진 단어의 합의 최댓값
num = 10 # 부여하고자 하는 숫자

for value in sortDict.values():
    num -= 1 # 9부터 부여
    result += value * num # 가중치 * num

print(result)