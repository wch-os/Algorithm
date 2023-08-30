import sys
input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 숫자 카드 개수
nList = list(map(int, input().split()))

M = int(input()) # 비교 대상의 숫자 카드 개수
mList = list(map(int, input().split()))

dict = {}
for n in nList:
    dict[n] = 1 # n은 key로 dictionary에 저장

result = []
for m in mList:
    if m not in dict: # m과 dict의 key를 대조해서 없으면 0
        result.append(0)

    else: # 있으면 1
        result.append(1)

print(' '.join(map(str, result)))