import sys

# 영어 지문에 나오는 단어의 개수, 단어의 길이 기준
N, M = map(int, sys.stdin.readline().split())

words = dict()
for _ in range(N):
    w = sys.stdin.readline().rstrip()

    if len(w) >= M:
        # w 키 값이 없으면 0 초기화, +1
        words[w] = words.get(w, 0) + 1

# 자주 나오는 단어를 기준으로 내림차순 정렬 : -item[1]
# 단어의 길이가 길수록 내림차순 정렬 : -len(item[0])
# 알파벳 사전순 정렬 : item[0]
sort_words = dict(sorted(words.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for key in sort_words.keys():
    print(key)