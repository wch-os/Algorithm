import sys
input = sys.stdin.readline

input_ = input().rstrip()
q = int(input().rstrip())

# 키보드 숫자 횟수 '0' 초기화
alphabet = dict()
for i in range(26):
    alphabet[chr(ord('a')+i)] = 0


# 인덱스 1 기준
# SUM[0] : input_에서 0번째 인덱스까지 각 문자가 나타나는 횟수므로, 모든 횟수가 0
# SUM[i] : i인덱스까지 각 문자가 나타나는 횟수
SUM = [alphabet.copy()]

for s in input_:
    alphabet[s] += 1
    SUM.append(alphabet.copy())

for _ in range(q):
    s, l, r = map(str, input().rstrip().split())
    l = int(l)
    r = int(r)

    # 문제에서 0인덱스 기준으로, 범위를 주니
    # 코드에서 1인덱스 기준으로, 설정해준다.

    # input_의 l번째 문자부터 r번째 문자 사이에 있는 s가 나타나는 횟수
    # SUM[r] - SUM[l-1]
    result = SUM[r+1][s] - SUM[l][s]
    print(result)