# 풀이 시간: 20분(다른 풀이) + 20분(생각) + 20분(참고)
# 시간복잡도: O(N)
# 공간복잡도: O(N)
# 유형: 백트래킹
# 참고: https://lu-coding.tistory.com/74

# 1
# 1 2
# 1 2 1
# 1 2 1 3
# 1 2 1 3 1
# 1 2 1 3 1 2
# 1 2 1 3 1 2 1
# 1 2 1 3 1 2 3 1
# 1 2 1 3 1 2 3 1 3
# 1 2 1 3 1 2 3 1 3 2
# 1 2 1 3 1 2 3 1 3 2 1

# 규칙 없음

N = int(input())
lst = []

def check():
    endIdx = len(lst)
    # 마지막 인덱스를 기준으로, 길이를 1부터 시작하여 수열의 길이//2 + 1 까지 좋은 수열인지 체크
    for i in range(1, len(lst) // 2 + 1):
        if lst[endIdx-i:endIdx] == lst[endIdx-i-i:endIdx-i]:
            return False # 나쁜 수열

    return True # 좋은 수열

def solve(idx):
    if idx == N:
        print(*lst, sep="")
        exit()

    for k in [1, 2, 3]:
        lst.append(k)
        if check(): # 좋은 수열인 경우 계속해서 탐색
            solve(idx + 1)
        lst.pop()

solve(0)