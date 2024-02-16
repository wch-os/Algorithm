# 풀이 시간 : 17분 + 5분 + 5분
# 시간복잡도 : O(p * n = 패턴 길이 * 문자열 길이)
# 공간복잡도 : O(n)
# 참고 : -

# 패턴에 있는 문자 중에 '*'을 제외한 알파벳 소문자와 '.'이 순서대로 있는지 파악하자.
# '*'을 기준으로 split 해야 한다.
    # 이전 코드에서는 패턴 '*abc*'일 경우 문자 'akbc'를 형식에 맞다고 판단한다.
# 문자일 경우 string의 끝 범위와 비교해야 함.
# 1이 아닌, p의 길이만큼 idx 시작 범위를 늘려줘야 함

# import sys
# input = sys.stdin.readline

def check():
    idx = 0
    isFind = True

    # 패턴 앞에 '*'가 아닌 일반 문자가 왔을 때
    if pattern[0] != '' and pattern[0] != string[:len(pattern[0])]:
        return False

    # 패턴 끝이 '*' 이거나, 문자일 경우 string의 끝 범위와 같은 경우
    elif pattern[-1] == '' or pattern[-1] == string[len(string)-len(pattern[-1]):]:
        for p in pattern:
            if p == '':
                continue

            # p 문자 찾기
            idx = string.find(p, idx, len(string))

            # 해당 문자가 없다면
            if idx == -1:
                isFind = False
                break

            idx += len(p) # 그 다음 인덱스부터 탐색

        return isFind

    # 틀리면 False
    else:
        return False


# 패턴
pattern = input()
pattern = pattern.split("*") # '*'을 기준으로 split

# 디렉토리 파일 갯수
N = int(input())

result = []
for _ in range(N):
    string = input()

    if check():
        result.append(string)

for r in result:
    print(r)