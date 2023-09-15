import sys
input = sys.stdin.readline

N = int(input()) # 숫자 카드의 개수

s = input()

# 입력 문자열을 split()으로 분할해, dictionary로 변환
# key : 문자 / value : 횟수
_dict = {}
for num in s.split():
    num = int(num)

    if num in _dict:
        _dict[num] += 1
    else:
        _dict[num] = 1


M = int(input())
c_s = input()
result = []
for num2 in c_s.split():
    num2 = int(num2)

    # 포함되어 있으면, 횟수 그대로 출력
    if num2 in _dict:
        result.append(_dict[num2])
    # 없으면 0 출력
    else:
        result.append(0)

print(' '.join(map(str, result)))